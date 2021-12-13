# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
	_inherit='product.template'

	product_group = fields.Selection(string='Product Group',
									 selection=[('g1, G1'),
									 			('g2','G2'),
									 			('g3','G3')])

	barcode = fields.Char(string='Barcode',
						  compute='_generate_barcode')

	@api.onchange('product_group')
	def _generate_barcode(self):
		p_group_str = str(self.product_group)
		self.barcode = p_group_str[0:2] + self.product_variant