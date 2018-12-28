# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from datetime import timedelta


class SessionModel(models.Model):
    _name = 'session.model'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(string="End Date", store=True,
                           compute="_get_end_date",
                           inverse="_set_end_date")
    datetime_test = fields.Datetime(default=fields.Datetime.now)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    # filtrar instructores por empresa formadora
    instructor_id = fields.Many2one("res.partner",
                                    string="Instructor",
                                    domain=[('instructor',
                                             '=', True)])
    course_id = fields.Many2one('course.model',
                                ondelete="cascade",
                                string="Course", required=True)
    attendee_ids = fields.Many2many("res.partner", string="Attendee")
    taken_seats = fields.Float(compute="_taken_seats")
    active = fields.Boolean(default=True)
    attendee_count = fields.Integer(compute="_get_attendee_count",
                                    store=True)
    color = fields.Float()
    hours = fields.Float(store=True, string="Duration in Hours",
                         compute="_get_hours", inverse="_set_hours")

    @api.depends('duration')
    def _get_hours(self):
        """
        Changing the duration field in days fills de duration in
        hours.

            * ``filtered`` function: Select the records in ``self``
            such that ``func(rec)`` is true, and return them as a
            recordset.

        :return: a float field

        """
        for record in self.filtered('duration'):
            record.hours = record.duration * 24

    def _set_hours(self):
        """
        Changing the duration field in hours fills de duration in
        days.

        :return: a float field
        """
        for session_time in self.filtered('duration'):
            session_time.duration = session_time.hours / 24

    @api.depends('attendee_ids')
    def _get_attendee_count(self):
        """
        Computed field that calculate the total number of
        attendees.

        :return: a integer field
        """
        self.attendee_count = len(self.attendee_ids)

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        """

        :return:
        """
        for record in self.filtered('start_date'):
            start_date = fields.Datetime.from_string(
                record.start_date)
            record.end_date = start_date + timedelta(
                days=record.duration, seconds=-1)

    @api.depends('start_date', 'end_date')
    def _set_end_date(self):
        """

        :return:
        """
        for record in self.filtered('start_date'):
            start_date = fields.Datetime.from_string(
                record.start_date)
            end_date = fields.Datetime.from_string(record.end_date)
            record.duration = (end_date - start_date).days + 1

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        """

        :return:
        """
        for record in self.filtered(lambda r: r.seats != 0):
            record.taken_seats = 100.0 * len(
                record.attendee_ids) / record.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        """

        :return:
        """
        if self.seats < 0:
            self.active = False
            return {
                'warning': {
                    'title': _('Incorrect seats Value'),
                    'message': 'Incorrect of seats may not be '
                               'negative '
                }
            }
        if self.seats < len(self.attendee_ids):
            self.active = False
            return {
                'warning': {
                    'title': _('To many attendees'),
                    'message': 'Increment seats or remove attendees '
                }
            }
        self.active = True

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        """

        :return:
        """
        for record in self.filtered('instructor_id'):
            if record.instructor_id in record.attendee_ids:
                raise exceptions.ValidationError(
                    "Asession instructor cant be an attendee")

    @api.multi
    def write(self, vals):
        """

        :param vals: {'field': value}
                ~ For example: {'seats': 51}

        :return: a boolean value.
        """
        if not self:
            return True
        print("Enter the write function every time you edit and "
              "save a record.")

        return True

    @api.model
    def create(self, vals):
        """

        :param vals:
        :return:
        """
        print("Enter the create function every time you create a new"
              "record")

        # Example super() call
        result = super(SessionModel,self).create(vals)

        #condition example
        if 'instructor_id' in vals:
            instr = vals['instructor_id']

            #instance example
            instructor = self.env['res.partner'].browse(instr)

            if instructor.parent_id and instructor.parent_id.name:
                print("Company name ---> ", instructor.parent_id.name)

        return result


