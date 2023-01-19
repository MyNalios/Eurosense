from odoo import api, fields, models

class Hr_Employee(models.Model):
    _inherit = 'hr.employee'

    allowed_timesheets_user_ids = fields.Many2many('hr.employee', 'hr_employee_allowed_employee_rel', 'employee_one_id', 'employee_two_id', string="Allowed timesheets users")

    