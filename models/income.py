from odoo import models, fields


class Income(models.Model):
    _name = 'gestor_income'
    _description = 'Ingreso de Evento'
    _rec_name = 'concept'

    concept = fields.Char(string='Concepto', required=True)
    amount = fields.Float(string='Importe', required=True)
    payment_date = fields.Date(string='Fecha de ingreso', required=True)
    payment_status = fields.Selection([
        ('pending', 'Pendiente'),
        ('paid', 'Pagado'),
    ], string='Estado del pago', default = 'pending')

    # Relaciones
    event_id = fields.Many2one('gestor.event', string='Evento Relacionado', required=True, ondelete='cascade')
    ticket_id = fields.Many2one('gestor.ticket', string='Ticket Asociado', ondelete='set null')
    