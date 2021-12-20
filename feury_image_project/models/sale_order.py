# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
	_inherit='sale.order'

	mrp_order_ids = fields.One2many('mrp.production', 'sale_order_id', string='Manufacturing Order Ids')

	num_mrp_orders = fields.Integer(string='Number of MOs for this sale order', compute='_compute_num_mrp_orders')


	def _compute_num_mrp_orders(self):
		for record in self:
			record.num_mrp_orders = len(record.mrp_order_ids)

	def get_mrp_orders(self):
		return self.mrp_order_ids