# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CharlaCharla(models.Model):
    # _inherit = 'event.event'
    _name = 'charla_clara.charla'
    _description = 'Charla Clara'

    name = fields.Char(string='Título', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    lugar = fields.Many2one("charla_clara.lugar", string="Lugar", ondelete="set null", required=True)

    tipo = fields.Selection(
        string="Tipo de Charla",
        selection=[
            ('P', "Pública"),
            ('CI', "Privada, con invitación"),
            ('S', "¿Qué charla? *le guiña un ojo*")],
            required=True,
            default='P'
    )

    currency_id = fields.Many2one('res.currency', string='Moneda')
    precio = fields.Monetary(string='Precio', required=True)

    ponente = fields.Many2one("res.users", string="Ponente", required=True)

    duracion = fields.Float(string='Duracion (minutos)', required=True)
    sinopsis = fields.Text(string="Sinopsis")
    asistentes_confirmados = fields.Integer(string='Asistentes confirmados', required=True)

    ganancias_totales = fields.Float(compute='_compute_ganancias_totales', readonly=True)
    @api.depends('precio', 'asistentes_confirmados')
    def _compute_ganancias_totales(self):
        for record in self:
            record.ganancias_totales = record.precio*record.asistentes_confirmados
