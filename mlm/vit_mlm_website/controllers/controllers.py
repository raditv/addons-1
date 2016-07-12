# -*- coding: utf-8 -*-
from openerp import http, SUPERUSER_ID
from openerp.http import request
import base64
import simplejson
from openerp.addons.website.models.website import slug


class Member(http.Controller):
	@http.route('/mlm/',  auth='public', website=True)
	def index(self, **kw):
		message_error = kw.get('message_error', '')
		message_success = kw.get('message_success', '')

		return http.request.render('vit_mlm_website.mlm_homepage', {
			'message_error':message_error,
			'message_success':message_success,
		})

	@http.route('/mlm/member/tree/',  auth='public', website=True)
	def tree(self, **kw):
		Members = http.request.env['res.partner']
		return http.request.render('website.tree', {
			'members': Members.search([('parent_id','=',False),('path','<>',False)])
		})

	@http.route('/mlm/member/list', auth='user', website=True)
	def list(self, **kw):		
		Partners = http.request.env['res.partner']
		Mymembers = self._cari_users_members(request.cr, request.uid, request.uid, request.context)
		return http.request.render('website.member_list', {
			'members': Partners.search([('id','in',Mymembers)])
		}) 

	@http.route('/mlm/member/view/<model("res.partner"):member>',  auth='user', website=True)
	def view(self, member):
		# Member = http.request.env['res.partner']
		# Paket  = http.request.env['mlm.paket']
		# State = http.request.env['res.country.state']
		# Country = http.request.env['res.country']
		# Products  = http.request.env['mlm.paket_produk']
		return http.request.render('website.member_view', {
			'member': member,
			'products': member.paket_produk_ids,
			# 'members': Member.search([]),
			# 'pakets': Paket.search([]),
			# 'states': State.search([]),
			# 'countrys': Country.search([]),
		})

	@http.route('/mlm/member/json/<int:parent_id>',  auth='user', website=True)
	def json(self, parent_id):
		Members = http.request.env['res.partner']
		members = Members.search([('parent_id','=',parent_id)])
		return members

	@http.route('/mlm/stockist',  auth='public', website=True)
	def stockist(self, **kw):
		Members = http.request.env['res.partner']
		members = Members.search([('is_stockist','=',True)])
		return http.request.render('website.member_list', {
			'members': members
		})

	@http.route('/mlm/member/create',  auth='user', website=True)
	def create(self, **kwargs):
		cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
		
		Users  = pool['res.users']
		user   = Users.browse(cr, uid, uid, context=context)
		parent = user.partner_id

		Member  = http.request.env['res.partner']
		Paket  = http.request.env['mlm.paket']
		State = http.request.env['res.country.state']
		Country = http.request.env['res.country']
		Products  = http.request.env['mlm.paket_produk']
		Mymembers = self._cari_users_members(cr, uid, uid, context)

		default_paket = Paket.search([('code','=','X')])
		values = {}
		for field in ['name', 'sponsor_id', 'parent_id', 'paket_id', 'street', 
			'street2', 'zip', 'city', 'state_id', 'country_id', 'bbm', 'email', 
			'phone','fax','mobile','paket_produk_id','signature','paket_produk_ids']:
			if kwargs.get(field):
				values[field] = kwargs.pop(field)
		values.update(kwargs=kwargs.items())
		values.update({
			'default_parent' : parent,
			'member' : None, # new member
			'pakets' : Paket.search([]),
			'default_paket': default_paket,
			'members': Member.search([('id','in',Mymembers)]),
			'states': State.search([]),
			'countrys': Country.search([]),
			'products': Products.search([]),

		})
		return http.request.render('website.member_create', values)

	def create_partner(self, request, values, kwargs):
		""" Allow to be overrided """
		pid= request.registry['res.partner'].create(request.cr, SUPERUSER_ID, values, request.context)
		return request.registry['res.partner'].browse(request.cr, SUPERUSER_ID, pid, request.context )

	def add_partner_response(self, values, kwargs):
		return request.website.render(kwargs.get("view_callback", "website.add_member_thanks"), values)

	@http.route('/mlm/member/add',  auth='user', method=['POST'], website=True)
	def add_member(self, **kwargs):
		cr, uid, context, pool = request.cr, request.uid, request.context, request.registry

		def dict_to_str(title, dictvar):
			ret = "\n\n%s" % title
			for field in dictvar:
				ret += "\n%s" % field
			return ret

		_TECHNICAL = ['show_info', 'view_from', 'view_callback']  # Only use for behavior, don't stock it
		_BLACKLIST = ['id', 'create_uid', 'create_date', 'write_uid', 'write_date', 'user_id', 'active']  # Allow in description
		_REQUIRED = ['name']  # Could be improved including required from model

		post_file = []  # List of file to add to ir_attachment once we have the ID
		post_description = []  # Info to add after the message
		values = {}
		paket_produk_ids = []
		for field_name, field_value in kwargs.items():
			if hasattr(field_value, 'filename'):
				post_file.append(field_value)
				if field_name=='signature':
					values['signature'] = base64.encodestring(field_value.read())
			elif field_name in request.registry['res.partner']._fields and field_name not in _BLACKLIST:
				values[field_name] = field_value
			elif field_name[:16] == 'paket_produk_ids' and field_value:
				paket_produk_ids.append((0,0,{'paket_produk_id':int(field_name[17:-1]),'qty':int(field_value)}))
			elif field_name not in _TECHNICAL:  # allow to add some free fields or blacklisted field like ID
				post_description.append("%s: %s" % (field_name, field_value))
				values[field_name] = field_value
		if paket_produk_ids:
			values['paket_produk_ids'] = paket_produk_ids
		error = set(field for field in _REQUIRED if not values.get(field))

		if error:
			values = dict(values, error=error, kwargs=kwargs.items())
			return request.website.render(kwargs.get("view_from", "website.member_create"), values)

		if post_description:
			values['description'] += dict_to_str(_("Custom Fields: "), post_description)
		try:
			lead_id = self.create_partner(request, dict(values, user_id=False),kwargs)
		except Exception,e:
			error = str(e)
			return error + ". Press BACK button"

		values.update(lead_id=lead_id)
		if lead_id:
			for field_value in post_file:
				attachment_value = {
					'name': 'Signature of '+values['name']+':'+field_value.filename,
					'res_name': field_value.filename,
					'res_model': 'res.partner',
					'res_id': lead_id,
					'datas': values['signature'],
					'datas_fname': field_value.filename,
				}
				request.registry['ir.attachment'].create(request.cr, SUPERUSER_ID, attachment_value, context=request.context)

		return request.redirect('/mlm/member/view/%s'% (slug(lead_id)), code=301)

	@http.route('/mlm/member/edit/<model("res.partner"):member>',  auth='user', website=True)
	def edit(self, member, **kwargs):
		Member = http.request.env['res.partner']
		Paket  = http.request.env['mlm.paket']
		State = http.request.env['res.country.state']
		Country = http.request.env['res.country']

		return http.request.render('website.member_edit', {
			'member': member,
			'default_parent': member.parent_id,
			'members': Member.search([]),
			'pakets': Paket.search([]),
			'states': State.search([]),
			'countrys': Country.search([]),
			'kwargs':kwargs.items(),
		})

	@http.route('/mlm/member/update',  auth='user', method='post', website=True)		
	def update_member(self, **kwargs):
		id = int(kwargs['id'])
		try:
			request.registry['res.partner'].write(request.cr, SUPERUSER_ID, [id], kwargs, request.context)
		except Exception,e:
			error = str(e)
			return error + ". Press BACK button"
		return request.redirect('/mlm/member/view/%d'% (id), code=301)

	@http.route('/mlm/member/stockist',  auth='user', website=True)
	def stockist(self, **kw):
		cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
		domain = [('is_stockist', '=', True)]
		Partner = pool.get('res.partner')
		Partner_ids = Partner.search(cr, uid, domain, context=context)
		Partners = Partner.browse(cr, uid, Partner_ids, context=context)

		return http.request.render('website.member_list', {
			'members': Partners,
		})

	@http.route('/mlm/member/tree/<model("res.partner"):member>',  auth='user', website=True)
	def tree(self,member):
		return http.request.render('website.d3_member_tree', {
			'member': member,
		})

	def _cari_users_members(self,cr,uid,user_id,context=None):
		Users  = request.registry['res.users']
		user   = Users.browse(cr, uid, user_id, context=context)
		path   = user.partner_id and user.partner_id.path
		partner_uid = user.partner_id and user.partner_id.id
		sql="select id from res_partner where path_ltree <@ '%s' \
			or (path_ltree is null and sponsor_id = %d) or (path_ltree is null and parent_id = %d) \
			order by path_ltree" % (path,partner_uid,partner_uid)
		cr.execute(sql)
		member_ids = cr.fetchall()
		return [x[0] for x in member_ids]

	@http.route('/mlm/member/create/json/<int:country_id>',type='json')
	def json(self,country_id):
		cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
		cr.execute("select id, name from res_country_state where country_id = %d" % country_id)
		rows = cr.fetchall()
		data = simplejson.dumps(dict(rows))
		return data