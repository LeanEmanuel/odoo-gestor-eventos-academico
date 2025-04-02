# -*- coding: utf-8 -*-7
from odoo import models, fields

class Expense(models.Model):
    _name = 'gestor.expense'
    _description = 'Gastos de Evento'
    _rec_name = 'concept'
    _order = 'date desc'

    concept = fields.Char(string='Concepto', required=True)
    amount = fields.Float(string='Cantidad', required=True)
    date = fields.Date(string='Fecha', required=True)
    notes = fields.Text(string='Notas')

    event_id = fields.Many2one('gestor.event', string='Evento Relacionado', ondelete='set null')