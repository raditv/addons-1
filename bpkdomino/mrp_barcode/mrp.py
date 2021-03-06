# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
import time
import math
import datetime
import calendar
import os
import csv
import re
from operator import itemgetter
from itertools import groupby


class mrp_production(osv.osv):
    _inherit = "mrp.production"

    _columns = {
        'serialno'    :   fields.char("Serial Number"),
    }

class material_requirement_line(osv.osv):
    _inherit = 'material.requirement.line' 
    _columns = {
        'source': fields.char('Source',  select=True),
    }

class material_requirement(osv.osv):
    _inherit  = 'material.requirement'
    homedir = os.path.expanduser('~')

    _columns = {
        'barcode_data': fields.text('Barcode Data'),  
    }

    def plan_change(self, cr, uid, ids, plan_id):
        rqn = []
        if plan_id:
            setting = self.pool.get('mrp.barcode.setting').search(cr,uid,[('active','=',True)],limit=1,order='write_date')
            if not setting :
                raise osv.except_osv("Pengaturan Setting Barcode Belum Tersedia","Setting di Manufacturing -> Configuration -> Barcode Setting")
            val = self.pool.get('production.plan').browse(cr, uid, plan_id) 
            for x in val.plan_list:
                rqn.append({
                    'product_id': x.product_id.id,
                    'product_uom': x.product_id.uom_po_id.id,
                    'plan': x.qty,
                    'name': x.product_id.name,
                    'source':x.name,
                }) 
        return {'value': {'requirement_line': rqn}}

    def _create_barrcode(self, cr, uid, ids, product_id, context={}):
        lot_seq = self.pool.get('ir.sequence').get(cr,uid, 'stock.lot.serial')
        lot_id = self.pool.get('stock.production.lot').create(cr,uid,{'name':lot_seq,'product_id':product_id.id})
        return lot_id

    def _get_setting(self,cr,uid,ids,product_id,source,kolom,count,serialno):
        setting_obj = self.pool.get('mrp.barcode.setting')
        setting_id = setting_obj.search(cr,uid,[('active','=',True)],limit=1,order='write_date')
        sett_id = setting_obj.browse(cr,uid,setting_id,context=None)
        prod_obj = self.pool.get('product.product')
        prod_id = prod_obj.browse(cr,uid,product_id)
        ean = prod_id.ean13 or ' '
        sn = serialno or ' '
        attrs = ' '.join([x.name for x in prod_id.attribute_value_ids])
        result=''
        data = {
                    1:[attrs,prod_id.name[:25],sn,sn,source],
                    2:[source,sn,sn,prod_id.name[:25],attrs],
                    3:[source,sn,sn,prod_id.name[:25],attrs] }
        sett_kolom = [l.list for l in sett_id.result_ids if l.kolom == kolom] 
        if sett_kolom:
            if kolom==1 and count==0:
                result+='N\nR'+','.join([str(sett_id.initRX),str(sett_id.initRY)])
            for dat,res in zip(data[kolom],sett_kolom):
                res = res.split(',')
                count
                res[1]=str(int(res[1])+sett_id.deltaY*int(count/3))
                # import pdb;pdb.set_trace()
                res =  ','.join(res)+'\"'+dat+'\"'
                result+=res
        return result

    def compute(self, cr, uid, ids, context={}):
        data = self.browse(cr, uid, ids)[0] 
        mrp_obj = self.pool.get("mrp.production")
        pr_obj = self.pool.get("purchase.requisition")
        type_obj = self.pool.get("stock.picking.type")
        bom_obj = self.pool.get("mrp.bom")
        categ_obj = self.pool.get("product.category")
        barang_booking =[];sum_barang_booking=[]
        res = ''
        # mo_ids = [] 
        wip = categ_obj.search(cr,uid,[('name','ilike','wip')])
        if wip:
            wip+=categ_obj.search(cr,uid,[('parent_id','=',wip)])
        finish = categ_obj.search(cr,uid,[('name','ilike','finish')])
        if finish:
            finish+=categ_obj.search(cr,uid,[('parent_id','=',finish)])
        
        ##############################################################################################
        # Delete existing MO & PR
        ##############################################################################################
        if data.manufacture_line:
            mrp_obj.unlink(cr,uid,[x.id for x in data.manufacture_line],{})
        if data.requisition_line :
            pr_obj.unlink(cr,uid,[x.id for x in data.requisition_line])
        
        ##############################################################################################
        # Buatkan Semua MO setiap Production Plan kemudian divalidasi
        # Jika Stok Produk Kurang dari Plan, dibuatkan draft Purchase Requisition, 
        #   Barang yang di attach ke PR adalah tingkatan raw, 
        #   jika finish atau wip, akan dipecah menjadi beberapa raw material, 
        #   Semua raw material dijumlahkan
        # TODO: - validasi MO bisa dipisah button
        #       - Jika dipisah generate PR dijalankan saat validasi MO
        ##############################################################################################
       
        kolom=1
        count=0
        for rp in data.requirement_line:
            values = mrp_obj.product_id_change(cr, uid, [], rp.product_id.id, context={})['value']
            # Jika bds varian
            bom = bom_obj.search(cr,uid,[('product_id','=',rp.product_id.id)])
            # Jika bds Product Template (di BoM)
            if not bom:
                bom = bom_obj.search(cr,uid,[('product_tmpl_id','=',rp.product_id.product_tmpl_id.id)])
            
            if bom:
                for i in range(int(rp.plan)):
                    lot_id = self._create_barrcode(cr, uid, ids, rp.product_id, context={})
                    serialno=self.pool.get('ir.sequence').get(cr, uid, 'lot.sn.seq', context=None) or '/'
                    source = rp.source or ' '
                    sources=source+' - '+ (data.name or ' ')
                    values.update({
                        'product_id': rp.product_id.id,
                        'product_qty':1,
                        'location_src_id': mrp_obj._src_id_default(cr, uid, [], context={}),
                        'location_dest_id': mrp_obj._dest_id_default(cr, uid, [], context={}),
                        'requirement_id': ids[0],
                        'origin':sources,
                        'serialno':serialno,
                        }) 
                    new_mo = mrp_obj.create(cr,uid,values)
                    # mrp_obj.action_confirm(cr, uid, new_mo, context={})
                    # mo_ids += self.mo_and_cosolidate(cr, uid, new_mo)
                    res += self._get_setting(cr,uid,ids,rp.product_id.id,source,kolom,count,values['serialno'])
                    if kolom==3:kolom=1
                    else : kolom+=1
                    count+=1
                res+='\nP\n'
                data.write({'barcode_data': res})
            selisih = rp.plan - rp.product_id.qty_available
            if rp.plan > rp.product_id.qty_available:
                if wip and rp.product_id.categ_id.id in wip:
                    bomID = bom_obj.search(cr,uid,[('product_id','=',rp.product_id.id)])
                    if not bomID:
                        bomID = bom_obj.search(cr,uid,[('product_tmpl_id','=',rp.product_id.product_tmpl_id.id)])
                    if bomID:
                        for bom in bom_obj.browse(cr,uid,bomID[0]).bom_line_ids:
                            barang_booking.append({
                                'product_id'  :bom.product_id.id, 
                                'product_uom_id' :bom.product_uom.id,
                                'product_qty' :selisih * bom.product_qty,
                            })
                    else :
                        barang_booking.append({
                                'product_id'  :rp.product_id.id, 
                                'product_uom_id' :rp.product_uom.id,
                                'product_qty' :selisih,
                            })
                elif finish and rp.product_id.categ_id.id in finish:
                    bomID = bom_obj.search(cr,uid,[('product_id','=',rp.product_id.id)])
                    if not bomID:
                        bomID = bom_obj.search(cr,uid,[('product_tmpl_id','=',rp.product_id.product_tmpl_id.id)])
                    if bomID:
                        for bom in bom_obj.browse(cr,uid,bomID[0]).bom_line_ids:
                            if bom.product_id.categ_id.id in wip:
                                bomID2 = bom_obj.search(cr,uid,[('product_id','=',bom.product_id.id)])
                                if not bomID2:
                                    bomID2 = bom_obj.search(cr,uid,[('product_tmpl_id','=',bom.product_id.product_tmpl_id.id)])
                                if bomID2:
                                    for bom2 in bom_obj.browse(cr,uid,bomID2[0]).bom_line_ids:
                                        barang_booking.append({
                                            'product_id'  :bom2.product_id.id, 
                                            'product_uom_id' :bom2.product_uom.id,
                                            'product_qty' :selisih * bom.product_qty * bom2.product_qty,
                                        })
                            elif bom.product_id.categ_id.id not in wip:
                                barang_booking.append({
                                    'product_id'  :bom.product_id.id, 
                                    'product_uom_id' :bom.product_uom.id,
                                    'product_qty' :selisih * bom.product_qty,
                                })
                    else :
                        barang_booking.append({
                            'product_id'  :rp.product_id.id, 
                            'product_uom_id' :rp.product_uom.id,
                            'product_qty' :selisih,
                        })
                else :
                    barang_booking.append({
                        'product_id'  :rp.product_id.id, 
                        'product_uom_id' :rp.product_uom.id,
                        'product_qty' :selisih,
                    })
        if barang_booking :
            # sum_barang_booking = []
            for k,itr in groupby(sorted(barang_booking, key=itemgetter('product_id')),itemgetter('product_id')):
                jml=0
                for v in itr: jml+=v['product_qty']
                sum_barang_booking.append([0,0,{
                        'product_id'  :k, 
                        'product_uom_id' :v['product_uom_id'],
                        'product_qty' :jml,
                    }])
            # cek warehouse di type_id, di pr origin ada 2, schedule date ada 2
        type_id = self.pool.get("stock.picking.type").search(cr,uid,[('name','ilike','Receipts'),('warehouse_id','=',1)])
        pr_obj.create(cr,uid,{
            "name" : self.pool.get('ir.sequence').get(cr, uid, 'purchase.order.requisition'),
            "origin" : data.name,
            "exclusive" : 'multiple',
            "line_ids"  : sum_barang_booking,
            "user_id" : self.pool.get('res.users').browse(cr, uid, uid, context).id, 
            "requirement_id" : ids[0],
            "picking_type_id" : type_id[0], 
            "warehouse_id" : 1,},context=None)
        return True


class mrp_barcode_setting_list(osv.osv):
    _name = 'mrp.barcode.setting.list'
    _columns = {
        'kolom':fields.integer("Kolom"),
        'list':fields.char('Setting'),
        'type'      : fields.selection([('A',"Label"),('B','Barcode')],'Type'),
        'setting_id': fields.many2one('mrp.barcode.setting','Setting') ,
    }


class mrp_barcode_setting_line(osv.osv):
    _name = 'mrp.barcode.setting.line'
    _columns = {
        'urutan'    : fields.integer('Sequence',help='Position relative to other line in column (Ascending).',size=2),
        'type'      : fields.selection([('A',"Label"),('B','Barcode')],'Type'),
        'rotation'  : fields.selection([('0','Normal'),('1','90 degree'),('2','180 degree'),('3','270 degree')],'Rotation'),
        'barcode'   : fields.selection([('1','Code 128 auto A,B,C modes'),('E30','EAN13')],'Barcode selection'),
        'height'    : fields.integer('Barcode height',size=2),
        'size'    : fields.selection([('1','Small'),('2','Medium')],'Label size'),
        'setting_id': fields.many2one('mrp.barcode.setting','Setting') ,
    }
    _defaults = {
        'rotation'  : '2',
    }


class mrp_barcode_setting_line2(osv.osv):
    _name = 'mrp.barcode.setting.line2'
    _columns = {
        'urutan'    : fields.integer('Sequence',help='Position relative to other line in column (Ascending).',size=2),
        'type'      : fields.selection([('A',"Label"),('B','Barcode')],'Type'),
        'rotation'  : fields.selection([('0','Normal'),('1','90 degree'),('2','180 degree'),('3','270 degree')],'Rotation'),
        'barcode'   : fields.selection([('1','Code 128 auto A,B,C modes'),('E30','EAN13')],'Barcode selection'),
        'height'    : fields.integer('Barcode height',size=2),
        'size'    : fields.selection([('1','Small'),('2','Medium')],'Label size'),
        'setting_id': fields.many2one('mrp.barcode.setting','Setting'), 
    }
    _defaults = {
        'rotation'  : '0',
    }


class mrp_barcode_setting(osv.osv):
    _name = 'mrp.barcode.setting'

    def compose_barcode(self, cr, uid, ids, context=None):
        vals = self.browse(cr,uid,ids[0],)
        content1 = []    
        content2 =[]    
        content3 = []    
        Ap4 = {'1':12,'2':'16'}
        Y1=0
        Y23=0
        list_obj = self.pool.get('mrp.barcode.setting.list')
        ul = [i.id for i in vals.result_ids]
        if ul :
            list_obj.unlink(cr, uid, ul , context=context)
        def construct_label(A,X,Y,R):
            return "\n"+",".join([A+X,Y,R,'1,1,1,N,'])
        def construct_barcode(B,X,Y,R,T,H):
            return "\n"+",".join([B+X,Y,R,T,'2,2',H,'N,'])
        if vals.detail_ids:
            for l in vals.detail_ids:
                if l.type == "A":
                    Y1+=int(Ap4[l.size])
                    str1 = construct_label("A",str(vals.initX1),str(Y1),l.rotation)
                else :
                    Y1+=int(l.height)+4
                    str1 = construct_barcode("B",str(vals.initX1),str(Y1),l.rotation,l.barcode,str(l.height))
                list_obj.create(cr,uid,{'setting_id':ids[0],'type' :l.type,'kolom':1,'list':str1})
        if vals.detail_ids2:
            for l in vals.detail_ids2:
                if l.type == "A":
                    str2 = construct_label("A",str(vals.initX2),str(Y23),l.rotation)
                    str3 = construct_label("A",str(vals.initX3),str(Y23),l.rotation)
                    Y23+=int(Ap4[l.size])
                else :
                    str2 = construct_barcode("B",str(vals.initX2),str(Y23),l.rotation,l.barcode,str(l.height))
                    str3 = construct_barcode("B",str(vals.initX3),str(Y23),l.rotation,l.barcode,str(l.height))
                    Y23+=int(l.height)+4
                list_obj.create(cr,uid,{'setting_id':ids[0],'type' :l.type,'kolom':2,'list':str2})
                list_obj.create(cr,uid,{'setting_id':ids[0],'type' :l.type,'kolom':3,'list':str3})
        return True

    _columns = {
        'name'      : fields.char('Name',size=10),
        'detail_ids2': fields.one2many('mrp.barcode.setting.line2','setting_id',string='Setting'),
        'detail_ids': fields.one2many('mrp.barcode.setting.line','setting_id',string='Setting'),
        'deltaY'    : fields.integer('Delta Y',size=3),
        'initX1'    : fields.integer('X0 column 1',size=3),
        'initX2'    : fields.integer('X0 column 2',size=3),
        'initX3'    : fields.integer('X0 column 3',size=3),
        'result_ids':fields.one2many('mrp.barcode.setting.list','setting_id',string='Setting',readonly=True),
        'active'    :fields.boolean("Active"),
        'initRX'    : fields.integer('X0 Form',size=3),
        'initRY'    : fields.integer('Y0 Form',size=3),
    }

    _defaults = {
        'deltaY'   :145,
        'initX1'    : 240,
        'initX2'    : 270,
        'initX3'    : 550,
        'active'    : True,
        'initRX'    : 0,
        'initRY'    : 0,
    }


class ProductionPlan(osv.osv):
    _inherit = 'production.plan'
    _columns = {
        'plan_list': fields.one2many('production.plan.list', 'plan_id', 'Production Plan List', readonly=True),
    }

    def compute(self, cr, uid, ids, context=None):
        val = self.browse(cr, uid, ids, context={})[0]
        product_obj = self.pool.get('product.product')
        def _create_list(ID,name,product,qty):
            self.pool.get('production.plan.list').create(cr,uid,{'plan_id':ID,'name':name,'product_id': product.id,'qty': qty,'ean13':product.ean13 or ''})
        if val.plan_line:
            for x in val.plan_line:
                plan = x.plan
                if x.real - x.total == 0 :
                    plan = x.max
                elif x.real - x.total <= 0 :
                    plan = abs(x.real - x.total) + x.max
                elif x.real - x.total < x.min:
                    plan = x.max - (x.real - x.total)
                self.pool.get('production.plan.line').write(cr, uid, [x.id], {'plan': plan, 'end': x.real - x.total + plan})
        else:
            product = []
            list_product = []
            for x in val.order_ids:
                for l in x.order_line:
                    product.append({'product_id': l.product_id.id, 'line': l, 'qty': l.product_uom_qty, 'uom': l.product_uom.id})
                    _create_list(val.id,x.name,l.product_id,l.product_uom_qty)
            for x in val.stock_ids:
                for l in x.stock_line:
                    product.append({'source':x.name,'product_id': l.product_id.id, 'line': l, 'qty': l.product_qty, 'uom': l.product_uom.id})
                    _create_list(val.id,x.name,l.product_id,l.product_qty)
            for x in val.stockw_ids:
                for l in x.stock_line:
                    product.append({'product_id': l.product_id.id, 'line': l, 'qty': l.product_qty, 'uom': l.product_uom.id})

            data = {}
            for p in product:
                data[p['product_id']] = {'qty': [], 'uom': p['uom'], 'line': []}
            for p in product:
                data[p['product_id']]['qty'].append(p['qty'])
                data[p['product_id']]['line'].append(p['line'])
            for i in data:
                order = sum(data[i]['qty'])
                brg = product_obj.browse(cr, uid, i)
                min = 0; max = 0; plan = order
                sid = self.pool.get('stock.warehouse.orderpoint').search(cr, uid, [('product_id', '=', i)])
                if sid:
                    sto = self.pool.get('stock.warehouse.orderpoint').browse(cr, uid, sid)[0]
                    min = sto.product_min_qty
                    max = sto.product_max_qty
                    plan = 0
                    if brg.qty_available - order == 0 :
                        plan = max
                    elif brg.qty_available - order <= 0 :
                        plan = abs(brg.qty_available - order) + max
                    elif brg.qty_available - order < min:
                        plan = max - (brg.qty_available - order)
                self.pool.get('production.plan.line').create(cr, uid, {
                                                                   'plan_id': val.id,
                                                                   'product_id': i,
                                                                   'product_uom': data[i]['uom'],
                                                                   'total': order,
                                                                   'name': product_obj.name_get(cr, uid, [i])[0][1],
                                                                   'real': brg.qty_available,
                                                                   'min': min,
                                                                   'max': max,
                                                                   'plan': plan,
                                                                   'end': brg.qty_available - order + plan 
                                                                   })
        return True 

ProductionPlan()

class production_plan_list(osv.osv):
    _name = 'production.plan.list' 
    _columns = {
        'name': fields.char('Source', readonly=True),
        'plan_id': fields.many2one('production.plan', 'Plan Reference', ondelete='cascade'),
        'product_id': fields.many2one('product.product', 'Product', readonly=True),
        'qty': fields.float('Total Order', readonly=True),
        'ean13':fields.char('ean13', readonly=True),
    }
