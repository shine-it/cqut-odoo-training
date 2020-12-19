# -*- coding: utf-8 -*-
# from odoo import http


# class Estate-property(http.Controller):
#     @http.route('/estate-property/estate-property/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estate-property/estate-property/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estate-property.listing', {
#             'root': '/estate-property/estate-property',
#             'objects': http.request.env['estate-property.estate-property'].search([]),
#         })

#     @http.route('/estate-property/estate-property/objects/<model("estate-property.estate-property"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estate-property.object', {
#             'object': obj
#         })
