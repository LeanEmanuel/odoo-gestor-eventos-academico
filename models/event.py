# -*- coding: utf-8 -*-
from odoo import models, fields


class Event(models.Model):
    _name = 'gestor.event'
    _description = 'Evento'
    _rec_name = 'name'

    name = fields.Char('Nombre del evento', required=True)
    description = fields.Text('Descripción')
    date_start = fields.Datetime('Fecha y hora de inicio', required=True)
    date_end = fields.Datetime('Fecha y hora de finalización', required=True)
    location = fields.Char('Ubicación')
    capacity = fields.Integer('Capacidad máxima')
    active = fields.Boolean('Activo', default=True)

    tickets = fields.One2many('gestor.ticket', 'event_id', string='Entradas')
    assistants = fields.One2many('gestor.assistant', 'event_id', string='Asistentes')
    category_id = fields.Many2one('gestor.category', string='Categoría')

    status = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('done', 'Finalizado'),
        ('cancelled', 'Cancelado'),
    ], string='Estado', default='draft')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Ya existe un evento con este nombre.')
    ]
