from odoo import models, fields, api

class smart_box(models.Model):
    _name = 'smart_box.box'

    localisation = fields.Char("Localisation")
    description = fields.Char("Description")
    num_box = fields.Char("Numéro box")

    enregistrement_ids = fields.One2many(comodel_name='smart_box.enregistrement', inverse_name='box_id')