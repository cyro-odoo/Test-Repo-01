# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MrpProduction(models.Model):
	_inherit='mrp.production'

	sale_order_id = fields.Many2one('sale.order', string='Sale Order')

	sale_order_line_id = fields.Many2one('sale.order.line', string='Sale Order Line')

	#sale_order_custom_notes = fields.Text(string="Sales Order Line Description", related='sale_order_line_id.custom_notes')

	