
from odoo import models, fields, api

class Paises(models.Model):
    _name = 'ordenadores.paises'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre del pais', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

