# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
	_inherit='product.template'

	allowed_contact_ids = fields.One2many(string='Allowed Contacts',
					      comodel_name='res.partner',
					      relation="allowed_product_buyer_rel")

	
