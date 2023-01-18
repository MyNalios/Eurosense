from odoo import api, fields, models

class Hr_Employee(models.Model):
    _inherit = 'hr.employee'

    allowed_timesheets_user_ids = fields.Many2many('hr.employee', string="Allowed timesheets users")

    