# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_type = fields.Selection([('consumer', 'Consumer'), ('patient','Patient'), ('caregiver','Caregiver'), ('external_patient', 'External Patient')])