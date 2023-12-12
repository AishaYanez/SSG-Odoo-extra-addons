# -*- coding: utf-8 -*-
# from odoo import http


# class Ssgproject(http.Controller):
#     @http.route('/ssgproject/ssgproject', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ssgproject/ssgproject/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ssgproject.listing', {
#             'root': '/ssgproject/ssgproject',
#             'objects': http.request.env['ssgproject.ssgproject'].search([]),
#         })

#     @http.route('/ssgproject/ssgproject/objects/<model("ssgproject.ssgproject"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ssgproject.object', {
#             'object': obj
#         })
