import logging
from collections import defaultdict
from functools import reduce

from odoo import models
from odoo.tools import populate

_logger = logging.getLogger(__name__)


class Material(models.Model):
    _inherit = "material.product"

    _populate_sizes = {'small': 450, 'medium': 15_000, 'large': 180_000}

    def _populate_get_types(self):
        return ["fabric", "jean","cotton"], [2, 1,2]

    def _populate_factories(self):
        types, types_distribution = self._populate_get_types()
        supplier_list = self.env['res.partner'].search([('supplier_rank','!=',0)]).ids

        def get_rand_float(values, counter, random):
            return random.randrange(101, 1500) 

        return [
            ("name", populate.constant('MP_{counter}')),
            ("code", populate.constant('MC_{counter}')),
            ("material_type", populate.randomize(types, types_distribution)),
            ("unit_price", populate.compute(get_rand_float)),
            ("partner_id", populate.randomize(supplier_list)),
        ]