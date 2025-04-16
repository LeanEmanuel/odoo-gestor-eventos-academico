# -*- coding: utf-8 -*-7
from datetime import date

from odoo import models, fields, api




class Expense(models.Model):
    _name = 'gestor.expense'
    _description = 'Gastos del Evento'
    _rec_name = 'concept'
    _order = 'date desc'

    concept = fields.Char(string='Concepto', required=True)
    amount = fields.Float(string='Importe', required=True)
    date = fields.Date(string='Fecha de gasto', required=True, default=lambda self: date.today())
    payment_status = fields.Selection([
        ('pending', 'Pendiente'),
        ('paid', 'Pagado'),
    ], string='Estado del pago', default='pending')
    payment_date = fields.Date(string="Fecha de pago")
    notes = fields.Text(string='Notas')

    event_id = fields.Many2one('gestor.event', string='Evento Relacionado', ondelete='set null')
    supplier_id = fields.Many2one('gestor.supplier', string="Proveedor")


    @api.onchange('payment_status')
    def _onchange_payment_status(self):
        if self.payment_status == 'paid' and not self.payment_date:
            self.payment_date = date.today()
