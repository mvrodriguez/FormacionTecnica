# -*- coding: utf-8 -*-

from odoo import models, fields


class Partner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many("session.model",
                                   string="Attended Session",
                                   readonly=True)
