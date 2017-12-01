# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools.translate import _

LIMIT_USER = 5
class res_users(models.Model):
    _inherit = 'res.users'
    # _description = 'Description'

    @api.model
    def create(self,vals):
    	users_ids = self.search([])
    	if len(users_ids) > LIMIT_USER:
    		raise UserError(_('You cannot create more than 5 user'))
    	return super(res_users,self).create(vals)