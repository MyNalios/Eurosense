# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrJob(models.Model):
    _inherit = 'hr.job'

    allowed_recruiter_ids = fields.Many2many('res.users', 'hr_job_allowed_recruiter_user_rel')


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    allowed_recruiter_ids = fields.Many2many('res.users', compute='_compute_allowed_recruiter_ids', store=True)

    @api.depends('job_id')
    def _compute_allowed_recruiter_ids(self):
        for rec in self:
            if rec.job_id.allowed_recruiter_ids:
                rec.allowed_recruiter_ids = [(6, 0, rec.job_id.allowed_recruiter_ids.ids)]
            else:
                rec.allowed_recruiter_ids = False
