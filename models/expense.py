# -*- coding: utf-8 -*-7
from datetime import date

from odoo import models, fields, api




class Expense(models.Model):
    _name = 'gestor.expense'
    _description = 'Gastos del Evento'
    _rec_name = 'concept'
    _order = 'date desc'

    # Basic expense data
    concept = fields.Char(string='Concepto', required=True)
    amount = fields.Float(string='Importe', required=True)
    date = fields.Date(string='Fecha de gasto', required=True, default=lambda self: date.today())

    # Payment tracking
    payment_status = fields.Selection([
        ('pending', 'Pendiente'),
        ('paid', 'Pagado'),
    ], string='Estado del pago', default='pending')
    payment_date = fields.Date(string="Fecha de pago")

    notes = fields.Text(string='Notas')

    # Relations
    event_id = fields.Many2one('gestor.event', string='Evento Relacionado', ondelete='set null')
    supplier_id = fields.Many2one('gestor.supplier', string="Proveedor")


    @api.onchange('payment_status')
    def _onchange_payment_status(self):
        """Automatically sets the payment_date to today when status is set to 'paid'."""
        if self.payment_status == 'paid' and not self.payment_date:
            self.payment_date = date.today()
