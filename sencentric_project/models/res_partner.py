# -*- coding: utf-8 -*-

from odoo import models, fields


class Partners(models.Model):
	_inherit='res.partner'

	allowed_product_ids = fields.One2many(string='Allowed Products',
					      comodel_name='product.template'
					      relation="allowed_product_buyer_rel")

	
