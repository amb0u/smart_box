# -*- coding: utf-8 -*-
from odoo import http

# class SmartBox(http.Controller):
#     @http.route('/smart_box/smart_box/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smart_box/smart_box/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_box.listing', {
#             'root': '/smart_box/smart_box',
#             'objects': http.request.env['smart_box.smart_box'].search([]),
#         })

#     @http.route('/smart_box/smart_box/objects/<model("smart_box.smart_box"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_box.object', {
#             'object': obj
#         })