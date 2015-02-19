# -*- coding: utf-8 -*-
from openerp import http, SUPERUSER_ID
from openerp.http import request

class Member(http.Controller):
	@http.route('/mlm/member/tree/',  auth='public', website=True)
	def index(self, **kw):
		Members = http.request.env['res.partner']
		return http.request.render('website.tree', {
			'members': Members.search([('parent_id','=',False),('path','<>',False)])
		})

	@http.route('/mlm/member/list', auth='user', website=True)
	def list(self, **kw):
		Members = http.request.env['res.partner']
		return http.request.render('website.member_list', {
			'members': Members.search([])
		})  

	@http.route('/mlm/member/view/<model("res.partner"):member>',  auth='user', website=True)
	def view(self, member):
		Member = http.request.env['res.partner']
		Paket  = http.request.env['mlm.paket']
		State = http.request.env['res.country.state']
		Country = http.request.env['res.country']
		return http.request.render('website.member_view', {
			'member': member,
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
		values = {}
		for field in ['name', 'sponsor_id', 'parent_id', 'paket_id', 'street', 
			'street2', 'zip', 'city', 'state_id', 'country_id', 'bbm', 'email', 
			'phone','fax','mobile']:
			if kwargs.get(field):
				values[field] = kwargs.pop(field)
		values.update(kwargs=kwargs.items())
		values.update({
			'parent' : parent,
			'member' : None,
			'pakets' : Paket.search([]),
			'members': Member.search([]),
			'states': State.search([]),
			'countrys': Country.search([]),

		})
		return http.request.render('website.member_create', values)

	def create_partner(self, request, values, kwargs):
		""" Allow to be overrided """
		return request.registry['res.partner'].create(request.cr, SUPERUSER_ID, values, request.context)

	def add_partner_response(self, values, kwargs):
		return request.website.render(kwargs.get("view_callback", "website.add_member_thanks"), values)

	@http.route('/mlm/member/add',  auth='user', method='post', website=True)
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

		for field_name, field_value in kwargs.items():
			if hasattr(field_value, 'filename'):
				post_file.append(field_value)
			elif field_name in request.registry['res.partner']._fields and field_name not in _BLACKLIST:
				values[field_name] = field_value
			elif field_name not in _TECHNICAL:  # allow to add some free fields or blacklisted field like ID
				post_description.append("%s: %s" % (field_name, field_value))

		error = set(field for field in _REQUIRED if not values.get(field))

		if error:
			values = dict(values, error=error, kwargs=kwargs.items())
			return request.website.render(kwargs.get("view_from", "website.member_create"), values)

		if post_description:
			values['description'] += dict_to_str(_("Custom Fields: "), post_description)

		lead_id = self.create_partner(request, dict(values, user_id=False), 
			kwargs)
		values.update(lead_id=lead_id)
		if lead_id:
			for field_value in post_file:
				attachment_value = {
					'name': field_value.filename,
					'res_name': field_value.filename,
					'res_model': 'crm.lead',
					'res_id': lead_id,
					'datas': base64.encodestring(field_value.read()),
					'datas_fname': field_value.filename,
				}
				request.registry['ir.attachment'].create(request.cr, SUPERUSER_ID, attachment_value, context=request.context)

		return request.redirect('/mlm/member/view/%d'% (lead_id), code=301)

	@http.route('/mlm/member/edit/<model("res.partner"):member>',  auth='user', website=True)
	def edit(self, member, **kwargs):
		Member = http.request.env['res.partner']
		Paket  = http.request.env['mlm.paket']
		State = http.request.env['res.country.state']
		Country = http.request.env['res.country']
		return http.request.render('website.member_edit', {
			'member': member,
			'parent': member.parent_id,
			'members': Member.search([]),
			'pakets': Paket.search([]),
			'states': State.search([]),
			'countrys': Country.search([]),
			'kwargs':kwargs.items(),
		})

	@http.route('/mlm/member/update',  auth='user', method='post', website=True)		
	def update_member(self, **kwargs):
		# import pdb; pdb.set_trace()
		id = int(kwargs['id'])
		request.registry['res.partner'].write(request.cr, SUPERUSER_ID, [id], kwargs, request.context)
		return request.redirect('/mlm/member/view/%d'% (id), code=301)
