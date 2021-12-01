from odoo import fields, api, models

class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    allowed_user_ids = fields.Many2many(string="Allowed users", comodel_name="res.users", relation="allowed_user_partner", column1="user_id", column2="partner_id", copy=False)