from odoo import api, fields, models

class Hr_Employee(models.Model):
    _inherit = 'hr.employee'

    allowed_timesheets_user_ids = fields.Many2many('res.users', string="Allowed timesheets users")

    