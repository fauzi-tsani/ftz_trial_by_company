# -*- coding: utf-8 -*-
from odoo import http

# class FzLimitUser(http.Controller):
#     @http.route('/fz_limit_user/fz_limit_user/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fz_limit_user/fz_limit_user/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fz_limit_user.listing', {
#             'root': '/fz_limit_user/fz_limit_user',
#             'objects': http.request.env['fz_limit_user.fz_limit_user'].search([]),
#         })

#     @http.route('/fz_limit_user/fz_limit_user/objects/<model("fz_limit_user.fz_limit_user"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fz_limit_user.object', {
#             'object': obj
#         })