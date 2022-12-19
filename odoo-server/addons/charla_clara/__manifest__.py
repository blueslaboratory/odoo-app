# -*- coding: utf-8 -*-
{
    'name': "Charlas Claras",

    'summary': """
        Módulo de charlas y ponencias en el instituto IES Clara del Rey
        """,

    'description': """
        Este módulo cuenta con 2 modelos: charla y lugar. Permite organizar charlas y ponencias, así como elegir su lugar o ver los asistentes del instituto IES Clara del Rey.
    """,

    'author': "Ronny Collaguazo & Alejandro Diez",
    'website': "https://iesclaradelrey.es/portal/index.php/es/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Marketing/Events',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # es el nombre del modulo del que depende
    'depends': ['event',
                'base',
                'website_slides',
                'hr'],

    # always loaded
    'data': [
        'security/charla_clara_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/reports.xml'
    ],

    # mostrarla en el cajon de aplicaciones:
    'application': True,
    # mostrarla la 1ra en el cajon de aplicaciones:
    'sequence': -100,
    # para permitir la instalacion del modulo:
    'installable': True,
}
