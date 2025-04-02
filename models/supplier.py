# -*- coding: utf-8 -*-
from odoo import models, fields


class Supplier(models.Model):
    _name = 'gestor.supplier'
    _description = 'Proveedor'
    _rec_name = 'name'

    name = fields.Char(string='Nombre del proveedor', required=True)
    contact_name = fields.Char(string='Persona de contacto')
    phone = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    address = fields.Text(string='Dirección')
    active = fields.Boolean(string='Activo', default=True)

    expense_ids = fields.One2many('gestor.expense', 'supplier_id', string='Gastos')
