# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


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

    @api.multi
    def generate_tickets(self):
        """
        Generate a predefined number of tickets for the event.
        """
        Ticket = self.env['gestor.ticket']
        try:
            ticket_type = self.env.ref('gestor_eventos.ticket_type_general', raise_if_not_found=False)
            if not ticket_type:
                ticket_type = self.env['gestor.ticket.type'].search([], limit=1)  # fallback
            for i in range(self.tickets_number):
                Ticket.create({
                    'event_id': self.id,
                    'ticket_type_id': ticket_type.id,
                    'price': 0.0,
                })
        except Exception as e:
            _logger.error("Error generating tickets for event %s: %s", self.name, str(e))
        return True

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
