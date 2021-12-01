from odoo import fields, models, api

class User(models.Model):
    _name = "res.users"
    _inherit = "res.users"

    allowed_contact_ids = fields.Many2many(string="Allowed partners", comodel_name="res.partner", relation="allowed_user_partner", column1="user_id", column2="partner_id", copy=False)