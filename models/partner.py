from odoo import fields, api, models

class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    allowed_users = fields.Many2many(string="Allowed users", comodel_name="res.users")