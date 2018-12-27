# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields


class CourseModel(models.Model):
    _name = 'course.model'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text()

    def default_responsible(self):
        return self.env.uid

    responsible_id = fields.Many2one('res.users',
                                     string="Responsible",
                                     Index=True,
                                     ondelete="set null",
                                     default=default_responsible)
    session_ids = fields.One2many('session.model', 'course_id')
