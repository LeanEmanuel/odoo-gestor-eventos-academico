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
    tag_ids = fields.Many2many(
        'gestor.tag',
        string='Etiquetas',
        help='Etiquetas asignadas al evento'
    )
    # Relaciones
    tickets = fields.One2many('gestor.ticket', 'event_id', string='Entradas')
    assistants = fields.One2many('gestor.assistant', 'event_id', string='Asistentes')
    category_id = fields.Many2one('gestor.category', string='Categoría')
    tag_ids = fields.Many2many('gestor.tag', string='Etiquetas')

    status = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('done', 'Finalizado'),
        ('cancelled', 'Cancelado'),
    ], string='Estado', default='draft')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Ya existe un evento con este nombre.')
    ]

    income_ids = fields.One2many('gestor.income', 'event_id', string='Ingresos')
    expense_ids = fields.One2many('gestor.expense', 'event_id', string='Gastos')

    total_income = fields.Float(string='Total Ingresos', compute='_compute_financials', store=True)
    total_expense = fields.Float(string='Total Gastos', compute='_compute_financials', store=True)
    balance = fields.Float(string='Balance', compute='_compute_financials', store=True)

    @api.depends('income_ids.amount', 'expense_ids.amount')
    def _compute_financials(self):
        for event in self:
            event.total_income = sum(event.income_ids.mapped('amount'))
            event.total_expense = sum(event.expense_ids.mapped('amount'))
            event.balance = event.total_income - event.total_expense
