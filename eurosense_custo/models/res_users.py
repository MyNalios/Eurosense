from odoo import api, fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    allowed_contact_ids = fields.Many2many('res.partner')