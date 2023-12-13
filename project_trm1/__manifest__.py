# -*- coding: utf-8 -*-
{
    'name': "Project_trm1",

    'summary': """
        Módulo de organización""",

    'description': """
        Sirve de apoyo para organizar proyectos, tareas y demás.
    """,

    'author': "Aisha",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','project'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,

    'assets': {
      'web.assets_common': [
        'project_trm1/static/src/scss/style1.scss',
      ]
    }
}
