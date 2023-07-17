from odoo import models, fields, api
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError


class Material(models.Model):
	_name = "material.product"
	_description = "Product Material"

	name = fields.Char(string="Material Name")
	code = fields.Char(string="Material Code")
	material_type = fields.Selection([
		('fabric','Fabric'),
        ('jean','Jeans'),
        ('cotton','Cotton'),
		],string="Material Type")
	unit_price = fields.Float(string="Material Buy Price")
	partner_id = fields.Many2one('res.partner',string="Supplier", domain="[('supplier_rank','!=',0)]")
	# Taik 
	# Kudo
	# Kapalo Kudo

	_sql_constraints = [('check_price','CHECK(unit_price > 100)','Buy Price must be above 100')]


