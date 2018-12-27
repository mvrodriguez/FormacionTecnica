from odoo import api, models


class ReportSession(models.AbstractModel):
    _name = "report.infodb_academia.report_session"

    @api.multi
    def render_html(self, docids, data=None):
        robj = self.env["report"]
        rep = robj._get_report_from_name(
            "infodb_academia.report_session")
        docargs = {
            "doc_ids": docids,
            "doc_model": rep.model,
            "docs": self.env['session.model'].browse(docids),
            "other_variable": 'other value'
        }
        return robj.render(
            "infodb_academia.report_session_view", docargs)
