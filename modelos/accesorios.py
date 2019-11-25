from odoo import models, fields

class Accesorios(models.Model):
    _name = 'ordenadores.accesorios'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required=True)
