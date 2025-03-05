# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gestor_eventos(models.Model):
#     _name = 'gestor_eventos.gestor_eventos'
#     _description = 'gestor_eventos.gestor_eventos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

