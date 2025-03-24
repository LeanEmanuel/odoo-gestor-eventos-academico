# -*- coding: utf-8 -*-
from odoo import models, fields


class Ticket(models.Model):
    _name = 'event.ticket'
    _description = 'Ticket de Evento'
    _rec_name = 'ticket_type'

    ticket_type = fields.Char(string='Tipo de ticket', required=True)
    price = fields.Float(string='Precio', required=True)
    qr_code = fields.Binary(string='QR Code')
    status = fields.Selection([
        ('available', 'Disponible'),
        ('sold', 'Vendida'),
        ('cancelled', 'Cancelada'),
    ], string='Estado', default='available')


    event_id = fields.Many2one('event.event', string='Evento relacionado', required=True, ondelete='cascade')
