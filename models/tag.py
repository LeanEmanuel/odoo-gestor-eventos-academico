from odoo import models, fields

class GestorTag(models.Model):
    _name = 'gestor.tag'
    _description = 'Etiqueta para eventos'
    _rec_name = 'name'

    name = fields.Char(string='Nombre de la etiqueta', required=True)
    color = fields.Integer(string='Color')

    event_ids = fields.Many2many('gestor.event', string='Eventos etiquetados')