# -*- coding: utf-8 -*-
# from odoo import http


# class Charlas-claras(http.Controller):
#     @http.route('/charlas-claras/charlas-claras', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/charlas-claras/charlas-claras/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('charlas-claras.listing', {
#             'root': '/charlas-claras/charlas-claras',
#             'objects': http.request.env['charlas-claras.charlas-claras'].search([]),
#         })

#     @http.route('/charlas-claras/charlas-claras/objects/<model("charlas-claras.charlas-claras"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('charlas-claras.object', {
#             'object': obj
#         })
