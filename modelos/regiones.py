from odoo import modelos, fields, api

class Regiones(modelos.Model):
    _name = 'ordenadores.regiones'
    region = fields.Char('Region', required=True)
    pais = fields.Many2one('ordenadores.paises', 'Paises')


    def name_get(self):
        res=[]
        for record in self:
            name = record.region
            res.append((record.id, name))
        return res

