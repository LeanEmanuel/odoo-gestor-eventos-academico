# -*- coding: utf-8 -*-
{
    'name': "Gestor de Eventos",

    'summary': "Módulo para la gestion de eventos de la asociación de vecinos.",

    'description': """
        Módulo en Odoo para la gestión de eventos, incluyendo:
        - Creación de eventos
        - Generación de tickets con QR
        - Control de asistencia
        - Gestión de ingresos y gastos
    """,

    'author': "Leandro Struni",
    'website': "https://github.com/LeanEmanuel",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/event_views.xml',
        'views/menu.xml',
        # 'views/views.xml',
        # 'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
