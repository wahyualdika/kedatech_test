from odoo.tests.common import TransactionCase
from odoo.tests import tagged
from odoo.exceptions import UserError


class MaterialTest(TransactionCase):

    def setUp(self):
        super(MaterialTest, self).setUp()
        self.properties = self.env['material.product'].create({
                'name' : 'Tes 2',
                'code' : '2ee4rr',
                'material_type' : 'blue',
                'unit_price' : 150,
                'partner_id' : 10,
            })

    def test_price(self):
        self.assertGreater(self.properties.unit_price,200,'Price must be higher than 100')


    def test_vendor(self):
        partner_status = self.env['res.partner'].browse(self.properties.partner_id.id)
        self.assertEqual(partner_status.supplier_rank, 1, "Partner is not a Vendor")


    # def test_material_type(self):
    #     self.assertIn(self.properties.material_type,['jean','cotton','fabric'],'Material Type is not registered')