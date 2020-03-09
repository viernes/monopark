from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    legal_representative = fields.Char('Representante Legal')
    type_document = fields.Selection([
        ('inx', 'INX'),('pasaporte', 'Pasaporte')
    ], 'Tipo de Documento')
    identifier = fields.Char('Numero de INX o Pasaporte')
    social_razn = fields.Char('Nombre comercial')



