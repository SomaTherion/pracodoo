from odoo import modelos, fields

class Impresoras(modelos.Model):
    _name = 'ordenadores.impresoras'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required=True)
