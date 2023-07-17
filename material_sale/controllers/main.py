from odoo import http
from odoo.http import request
import json
import logging

from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError

_logger = logging.getLogger(__name__)

class MaterialController(http.Controller):

    # Percobaan Controller RRR

    @http.route(['/material', '/material/<string:material_type>',],csrf=False, auth="public", methods=['get'])
    def get_material(self,material_type=None, **kwargs):
        res = []
        material = False
        if not material_type:
            materials = request.env['material.product'].sudo().search([])
            for material in materials:
                value = {
                    'name' : material.name,
                    'code': material.code,
                    'material_type': material.material_type,
                    'supplier':material.partner_id.name,
                    'unit_price':material.unit_price,
                }
                res.append(value)

        else:
            if material_type not in ['jean','cotton','fabric']:
                res.append('Material is not listed')
            materials = request.env['material.product'].sudo().search([('material_type','=',material_type)])
            for material in materials:
                value = {
                    'name' : material.name,
                    'code': material.code,
                    'material_type': material.material_type,
                    'supplier':material.partner_id.name,
                    'unit_price':material.unit_price,
                }
                res.append(value)

        return json.dumps(res)

    @http.route(['/material/<int:material_id>',],csrf=False, auth="public", methods=['post','put','patch'])
    def update_material(self,material_id=None, **kwargs):
        if material_id:
            material = request.env['material.product'].sudo().browse(material_id)
            result = self.check_available_data(kwargs)
            m = material.sudo().write(result)
            return json.dumps(m)
        else:
            return json.dumps([])


    @http.route(['/material/<int:material_id>',],csrf=False, auth="public", methods=['delete'])
    def update_material(self,material_id=None, **kwargs):
        if material_id:
            material = request.env['material.product'].sudo().browse(material_id)
            m = material.sudo().unlink()
            return json.dumps(m)
        else:
            return json.dumps([])


    def check_available_data(self,data):
        result = {}
        if data.get('name'):
            result.update({
                    'name': data.get('name')
                })
        if data.get('material_type'):
            result.update({
                'material_type': data.get('material_type')
            })
        if data.get('partner_id'):
            result.update({
                'partner_id': data.get('partner_id')
            })
        if data.get('price'):
            result.update({
                'unit_price': data.get('price')
            })
        return result
