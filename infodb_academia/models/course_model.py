# -*- coding: utf-8 -*-

from odoo import models
from odoo import fields

class CourseModel(models.Model):
    _name = 'course.model'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string="Responsible", Index=True, ondelete="set null", default=lambda self, *a: self.env.uid)
    session_ids = fields.One2many('session.model', 'course_id')
    

