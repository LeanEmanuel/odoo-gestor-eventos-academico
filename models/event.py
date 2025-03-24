# -*- coding: utf-8 -*-
from odoo import models, fields


class Event(models.Model):
    _name = 'event.event'
    _description = 'Evento'
    _rec_name = 'name'

    name = fields.Char('Nombre del evento', required=True)
    description = fields.Text('Descripción')
    date_start = fields.Datetime('Fecha y hora de inicio', required=True)
    date_end = fields.Datetime('Fecha y hora de finalización', required=True)
    location = fields.Char('Ubicación')
    capacity = fields.Integer('Capacidad máxima')
    active = fields.Boolean('Activo', default=True)

    tickets = fields.One2many('event.ticket', 'event_id', string='Entradas')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Ya existe un evento con este nombre.')
    ]
