# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CharlaLugar(models.Model):
    # _inherit = 'event.event'
    _name = 'charla_clara.lugar'
    _description = 'Lugar Charla'

    name = fields.Char(string='Lugar', required=True)

    # codigo_lugar, sirve para guardar un código.
    '''
    codigo_lugar = fields.Selection(
        string="Lugar de la Ponencia",
        selection=[
            ('ENSA', "Edificio Norte - Salon de Actos"),
            ('EN1A', "Edificio Norte - Planta 1 - Sala A"),
            ('ES2H', "Edificio Sur - Planta 2 - Sala H"),
            ('POLI', "Polideportivo")],
            default="POLI",
            required=True
    )
    '''
    aforo = fields.Integer(string='Aforo')
    imagen = fields.Binary(string='Imagen')
    parking_dis = fields.Boolean(string='Dispone de parking')
