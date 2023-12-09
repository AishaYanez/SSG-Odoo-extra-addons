# -*- coding: utf-8 -*-
# from odoo import http


# class ProyectTrm1(http.Controller):
#     @http.route('/proyect_trm1/proyect_trm1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyect_trm1/proyect_trm1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyect_trm1.listing', {
#             'root': '/proyect_trm1/proyect_trm1',
#             'objects': http.request.env['proyect_trm1.proyect_trm1'].search([]),
#         })

#     @http.route('/proyect_trm1/proyect_trm1/objects/<model("proyect_trm1.proyect_trm1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyect_trm1.object', {
#             'object': obj
#         })
