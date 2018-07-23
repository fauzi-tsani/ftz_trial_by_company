# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessDenied, UserError, ValidationError
from odoo.tools.translate import _
import datetime

class res_users(models.Model):
    _inherit = 'res.users'
    # _description = 'Description'

    # @api.model
    # def create(self,vals):
    # 	users_ids = self.search([])
    # 	if len(users_ids) > LIMIT_USER:
    # 		raise UserError(_('You cannot create more than 5 user'))
    # 	return super(res_users,self).create(vals)

    @api.model
    def check_credentials(self, password):
        """ Override this method to plug additional authentication methods"""
        print "="*10
        print self,password
        print self._uid,password
        # user = self.sudo().search([('id', '=', self._uid), ('password', '=', password)])
        # print user
        print self.company_id.is_trial and (self.company_id.trial_exp < str(datetime.datetime.now().date()))
        print self.company_id.is_trial , (self.company_id.trial_exp , str(datetime.datetime.now().date()))

        # if not user:
        #     raise AccessDenied()
        if self.company_id.is_trial and self.company_id.trial_exp:
            if self.company_id.trial_exp < str(datetime.datetime.now().date()):
        	   raise AccessDenied()

class res_company(models.Model):
    _inherit = 'res.company'

    is_trial = fields.Boolean(
        string='Is Trial',
        default=True
    )

    trial_exp = fields.Date(
        string='Trial Date Expire'
    )
    