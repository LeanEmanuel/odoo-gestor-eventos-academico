# -*- coding: utf-8 -*-
from odoo import models, fields


class Category(models.Model):
    _name = 'gestor.category'
    _description = 'Categoría de Evento'
    _rec_name = 'name'

    # Category name and optional description
    name = fields.Char(string='Nombre de la categoría', required=True)
    description = fields.Text(string='Descripción')

    # One-to-many relationship with events
    event_ids = fields.One2many('gestor.event', 'category_id', string='Eventos relacionados')
