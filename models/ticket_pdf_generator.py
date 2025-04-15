# -*- coding: utf-8 -*-
import base64
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from odoo import models, fields, api
from odoo.modules.module import get_module_resource
import logging

_logger = logging.getLogger(__name__)


class TicketPDFGenerator(models.AbstractModel):
    _name = 'report.gestor_eventos.ticket_pdf_report'
    _description = 'Generador de PDF para tickets de eventos'

    def generate_ticket_pdf(self, ticket_id):
        ticket = self.env['gestor.ticket'].browse(ticket_id)

        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        # Borde decorativo
        c.setStrokeColorRGB(0.2, 0.2, 0.2)
        c.setDash(6, 3)
        c.rect(2 * cm, 2 * cm, width - 4 * cm, height - 4 * cm)

        # --- Estilos ---
        title_style = ParagraphStyle('Title', fontName='Helvetica-Bold', fontSize=16, alignment=TA_LEFT, spaceAfter=10)
        info_style = ParagraphStyle('Info', fontName='Helvetica', fontSize=12, alignment=TA_LEFT)
        footer_style = ParagraphStyle('Footer', fontName='Helvetica', fontSize=10, alignment=TA_LEFT,
                                      textColor=colors.grey)

        # --- Posiciones base ---
        margin_x = 3 * cm
        margin_y = 4 * cm
        column_width = (width - 2 * margin_x) / 2
        top = height - margin_y

        # --- Imagen del evento (izquierda) ---
        default_image_path = get_module_resource('gestor_eventos', 'static/img', 'default-image.jpg')
        try:
            if ticket.event_id.image:
                event_img = BytesIO(base64.b64decode(ticket.event_id.image))
                img_reader = ImageReader(event_img)
            else:
                img_reader = ImageReader(default_image_path)
            c.drawImage(img_reader, margin_x, top - 8 * cm, width=8 * cm, height=8 * cm, preserveAspectRatio=True)
        except Exception as e:
            _logger.warning(f"No se pudo cargar ninguna imagen del evento: {e}")

        # --- Contenido del ticket (derecha) ---
        content_x = margin_x + column_width + 1 * cm
        content_y = top

        title = Paragraph(ticket.event_id.name or "", title_style)
        title.wrapOn(c, column_width - 1 * cm, 2 * cm)
        title.drawOn(c, content_x, content_y)

        entry = Paragraph(f"Entrada: {ticket.ticket_type}", info_style)
        entry.wrapOn(c, column_width - 1 * cm, 2 * cm)
        entry.drawOn(c, content_x, content_y - 1.5 * cm)

        code = Paragraph(f"Código: {ticket.code}", info_style)
        code.wrapOn(c, column_width - 1 * cm, 2 * cm)
        code.drawOn(c, content_x, content_y - 3 * cm)

        # Código QR centrado respecto a columna derecha
        if ticket.qr_code:
            qr_img = BytesIO(base64.b64decode(ticket.qr_code))
            qr_reader = ImageReader(qr_img)
            qr_size = 5 * cm
            qr_x = content_x
            qr_y = content_y - 9 * cm
            c.drawImage(qr_reader, qr_x, qr_y, width=qr_size, height=qr_size)

        # Nota inferior centrada
        footer = Paragraph(
            "Presenta esta entrada con su código QR al acceder al evento.<br/><b>No se permiten duplicados ni reembolsos.</b>",
            footer_style
        )
        footer.wrapOn(c, width - 4 * cm, 3 * cm)
        footer.drawOn(c, margin_x, 3 * cm)

        c.showPage()
        c.save()

        pdf = buffer.getvalue()
        buffer.close()
        return pdf


class Ticket(models.Model):
    _inherit = 'gestor.ticket'

    def generate_pdf_ticket(self):
        self.ensure_one()
        pdf = self.env['report.gestor_eventos.ticket_pdf_report'].generate_ticket_pdf(self.id)

        attachment = self.env['ir.attachment'].create({
            'name': f'Entrada_{self.code}.pdf',
            'datas': base64.b64encode(pdf),
            'type': 'binary',
            'res_model': 'gestor.ticket',
            'res_id': self.id,
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }
