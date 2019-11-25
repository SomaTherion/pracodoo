from odoo import modelos, fields

class Accesorios(modelos.Model):
    _name = 'ordenadores.accesorios'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required=True)
