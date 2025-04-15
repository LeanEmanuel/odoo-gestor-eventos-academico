# -*- coding: utf-8 -*-

import random
import string
import qrcode
import base64
from io import BytesIO
from odoo import models, fields, api


class Ticket(models.Model):
    _name = 'gestor.ticket'
    _description = 'Ticket de Evento'
    _rec_name = 'ticket_type'

    ticket_type = fields.Char(string='Tipo de ticket', required=True)
    price = fields.Float(string='Precio', required=True)
    code = fields.Char(string='Codigo único', required=False, readonly=True, copy=False, index=True)
    qr_code = fields.Binary(string='QR Code')
    status = fields.Selection([
        ('available', 'Disponible'),
        ('sold', 'Vendida'),
        ('cancelled', 'Cancelada'),
        ('validated','Validado'),
    ], string='Estado', default='available')

    # Relaciones
    event_id = fields.Many2one('gestor.event', string='Evento relacionado', required=True, ondelete='cascade')
    assistant_id = fields.Many2one('gestor.assistant', string='Asistente', ondelete='set null')

    @api.model
    def create(self, vals):
        if 'code' not in vals or not vals['code']:
            vals['code'] = self._generate_unique_code()
        res = super().create(vals)
        res._generate_qr_code()
        return res

    def _generate_unique_code(self, length=10):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choices(characters, k=length))

    def _generate_qr_code(self):
        for record in self:
            if record.code:
                qr = qrcode.QRCode(version=1, box_size=10, border=5)
                qr.add_data(record.code)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")

                buffer = BytesIO()
                img.save(buffer, format='PNG')
                qr_image = base64.b64encode(buffer.getvalue())
                record.qr_code = qr_image



