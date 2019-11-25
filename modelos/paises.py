
from odoo import modelos, fields, api

class Paises(modelos.Model):
    _name = 'ordenadores.paises'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre del pais', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

