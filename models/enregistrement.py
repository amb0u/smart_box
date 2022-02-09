from odoo import models, fields, api

class smart_box(models.Model):
    _name = 'smart_box.enregistrement'

    #Données des capteurs
    temperature = fields.Integer('Température')
    humidite = fields.Integer('Humidité')
    date = fields.Date('Date')

    #Données de la raspberry
    cpu = fields.Integer('CPU')
    temp = fields.Integer('Température Raspberry')
    memoire = fields.Date('Mémoire')

    box_id = fields.Many2one(comodel_name='smart_box.box', delegate=True, required=True)