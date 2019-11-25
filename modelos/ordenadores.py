from odoo import modelos, fields, api

class Ordenadores(modelos.Model):
    _name = 'ordenadores.ordenadores'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required=True)
    pais = fields.Many2one('ordenadores.paises', 'Paises')
    region = fields.Many2one('ordenadores.regiones', 'Regiones')



    @api.one
    def limpiar(self):
        self.marca = ""
        return True

    @api.multi
    def limpia_todo(self):
        done_recs = self.search([('marca', '=', 'fender')])
        done_recs.write({'marca': 'Fender'})
        return True

