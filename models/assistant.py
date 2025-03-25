from odoo import models, fields


class GestorAssistant(models.Model):
    _name = 'gestor.assistant'
    _description = 'Asistente de evento'
    _rec_name = 'name'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo electrónico')
    phone = fields.Char(string='Teléfono')
    dni = fields.Char(string='DNI')
    check_in = fields.Boolean(string='Asistió', default=False)
    check_in_time = fields.Datetime(string='Hora de entrada')

    ticket_id = fields.Many2one('gestor.ticket', string='Entrada', ondelete='set null')
    event_id = fields.Many2one('gestor.event', string='Evento', required=True, ondelete='cascade')
