# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

LIMIT_USER = 5
class res_users(models.Model):
    _inherit = 'res.users'
    # _description = 'Description'

    @api.models
    def create(self,vals):
    	users_ids = self.search([])
    	if len(users_ids) > LIMIT_USER:
    		raise UserError(_('You cannot create more user'))