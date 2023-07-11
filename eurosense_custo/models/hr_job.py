# -*- coding: utf-8 -*-

from odoo import models, fields


class HrJob(models.Model):
    _inherit = 'hr.job'

    allowed_recruiter_ids = fields.Many2many('res.users', 'hr_job_allowed_recruiter_user_rel')
