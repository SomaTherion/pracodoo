from odoo import models, fields

class Accesorios(models.Model):
    _name = 'ordenadores.tiendas'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required=True)
    pais = fields.Many2one('ordenadores.paises', 'Paises')
    region = fields.Many2one('ordenadores.regiones', 'Regiones')
