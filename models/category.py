from odoo import models, fields


class Category(models.Model):
    _name = 'gestor.category'
    _description = 'Categoría de Evento'
    _rec_name = 'name'

    name = fields.Char(string='Nombre de la categoría', required=True)
    description = fields.Text(string='Descripción')

    event_ids = fields.One2many('gestor.event', 'category_id', string='Eventos relacionados')
