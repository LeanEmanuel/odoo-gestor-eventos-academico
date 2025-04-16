# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class Event(models.Model):
    _name = 'gestor.event'
    _description = 'Evento'
    _rec_name = 'name'

    # Basic event information
    name = fields.Char('Nombre del evento', required=True)
    description = fields.Text('Descripción')
    date_start = fields.Datetime('Fecha y hora de inicio', required=True)
    date_end = fields.Datetime('Fecha y hora de finalización', required=True)
    location = fields.Char('Ubicación')
    capacity = fields.Integer('Capacidad máxima')

    # Ticket generation
    ticket_generation_qty = fields.Integer(
        string='Cantidad de tickets a generar',
        default=1,
        help="Número de tickets que se generaran para este evento."
    )

    active = fields.Boolean('Activo', default=True)

    # Tags and categories
    tag_ids = fields.Many2many(
        'gestor.tag',
        string='Etiquetas',
        help='Etiquetas asignadas al evento'
    )

    # Event image (used in PDFs or UI)
    image = fields.Binary(string='Cartel del evento', attachment=True)

    # Relations
    tickets = fields.One2many('gestor.ticket', 'event_id', string='Entradas')
    assistants = fields.One2many('gestor.assistant', 'event_id', string='Asistentes')
    category_id = fields.Many2one('gestor.category', string='Categoría')
    tag_ids = fields.Many2many('gestor.tag', string='Etiquetas')
    income_ids = fields.One2many('gestor.income', 'event_id', string='Ingresos')
    expense_ids = fields.One2many('gestor.expense', 'event_id', string='Gastos')

    # Event status
    status = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('done', 'Finalizado'),
        ('cancelled', 'Cancelado'),
    ], string='Estado', default='draft')

    # Campos calculados financieros
    total_income = fields.Float(string='Total Ingresos', compute='_compute_financials', store=True)
    total_expense = fields.Float(string='Total Gastos', compute='_compute_financials', store=True)
    balance = fields.Float(string='Balance', compute='_compute_financials', store=True)

    def generate_tickets(self):
        """
        Generate a predefined number of tickets for the event.
        Throws error if the quantity is invalid.
        """
        for event in self:
            quantity = event.ticket_generation_qty
            if quantity <= 0:
                raise UserError(_("La cantidad de tickets debe ser mayor que 0."))

            Ticket = self.env['gestor.ticket']
            for _ in range(quantity):
                Ticket.create({
                    'ticket_type': 'General',
                    'price': 0.0,
                    'event_id': event.id
                })

    @api.depends('income_ids.amount', 'expense_ids.amount')
    def _compute_financials(self):
        """
        Calculate total income, expenses, and net balance for the event.
        """
        for event in self:
            event.total_income = sum(event.income_ids.mapped('amount'))
            event.total_expense = sum(event.expense_ids.mapped('amount'))
            event.balance = event.total_income - event.total_expense

    # Unique constraint on event name
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Ya existe un evento con este nombre.')
    ]
