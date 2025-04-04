# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)


class TicketController(http.Controller):

    @http.route('/api/ticket/validate', type='json', auth='public', methods=['POST'], csrf=False)
    def validate_ticket(self):
        try:
            # Leer el cuerpo de la solicitud desde httprequest (raw)
            raw_data = request.httprequest.data
            data = json.loads(raw_data.decode('utf-8'))

            _logger.info("Datos recibidos: %s", data)

            code = data.get('code')
            if not code:
                return {'error': 'Ticket code is required'}

            # Buscar el ticket por el código
            ticket = request.env['gestor.ticket'].sudo().search([('code', '=', code)], limit=1)

            # Validar si no encuentra el ticket
            if not ticket:
                return {'error': 'Ticket not found'}

            # Validar si el ticket esta disponible
            if ticket.status != 'available':
                return {'error': 'Ticket is not available'}

            # Cambiar estado a validated
            ticket.sudo().write({'status': 'validated'})
            return {'message': 'Ticket successfully validated'}

        except Exception as e:
            _logger.error("Error al procesar validación del ticket: %s", str(e))
            return {'error': str(e)}
