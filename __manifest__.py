# -*- coding: utf-8 -*-
{
    'name': "Smart box",

    'summary': """
        Projet de monitoring d'une smart box""",

    'description': """
        Ce module permet de visualiser des données de capteurs
    """,

    'author': "Ambroise Ngagne TINE",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Monitoring',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/box.xml',
        'views/enregistrement.xml',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':'true',
}