# -*- coding: utf-8 -*-
# from odoo import http


# class GestorEventos(http.Controller):
#     @http.route('/gestor_eventos/gestor_eventos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestor_eventos/gestor_eventos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestor_eventos.listing', {
#             'root': '/gestor_eventos/gestor_eventos',
#             'objects': http.request.env['gestor_eventos.gestor_eventos'].search([]),
#         })

#     @http.route('/gestor_eventos/gestor_eventos/objects/<model("gestor_eventos.gestor_eventos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestor_eventos.object', {
#             'object': obj
#         })

