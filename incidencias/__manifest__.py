# -*- coding: utf-8 -*-
{
    'name': "incidencias",

    'summary': """
        Módulo de incidencias""",

    'description': """
        Registro de las incidencias en los municipios de Gran Canaria
    """,

    'author': "Aisha",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/municipios_report.xml',
        'reports/municipios_report_view.xml',
        'data/product_category_data.xml',
        'security/incidencias_reglas_registro.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,

    'assets': {
      'web.assets_common': [
        'incidencias/static/src/scss/style1.scss',
      ],
    }
}
