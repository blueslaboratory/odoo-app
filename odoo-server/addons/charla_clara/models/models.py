from odoo import models, fields, api


class CharlaAuditorio(models.Model):
    _inherit = 'event.event'

    # Drop down: menu desplegable

    charla_sala = fields.Selection(
        string="Lugar de la Ponencia",
        selection=[
            ('ENSA', "Edificio Norte - Salon de Actos"),
            ('EN1A', "Edificio Norte - Planta 1 - Sala A"),
            ('ES2H', "Edificio Sur - Planta 2 - Sala H"),
            ('POLI', "Polideportivo")],
            default="POLI"
    )
