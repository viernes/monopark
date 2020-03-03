# -*- coding: utf-8 -*-
from odoo import http

# class ../extra-addons/xmarts/monopark/saleSimplifier/saleSimplifier/(http.Controller):
#     @http.route('/../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier//../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier//../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier/.listing', {
#             'root': '/../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier//../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier/',
#             'objects': http.request.env['../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier/.../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier/'].search([]),
#         })

#     @http.route('/../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier//../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier//objects/<model("../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier/.../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../extra-addons/xmarts/monopark/sale_simplifier/sale_simplifier/.object', {
#             'object': obj
#         })