# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/infodb_academia/cursos', type='http', auth='none')
    def cursos(self):
        records = request.env['course.model'].sudo().search([])
        result = '<html><body><table><tr><td>'
        result += '</td></tr><tr><td>'.join(records.mapped('name'))
        result += '</td></tr></table></body></html>'
        return result

    @http.route('/infodb_academia/cursos/json', type='json', auth='none')
    def cursos_json(self):
        records = request.env['course.model'].sudo().search([])

        return records.read(['name'])