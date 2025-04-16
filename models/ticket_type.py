# -*- coding: utf-8 -*-
from odoo import models, fields


class TicketType(models.Model):
    _name = 'gestor.ticket.type'
    _description = 'Tipo de Ticket'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string='Nombre del tipo', required=True)
    description = fields.Text(string='Descripción')