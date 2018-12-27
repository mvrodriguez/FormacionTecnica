# -*- coding: utf-8 -*-
{
    'name': "formacion_tecnica",

    'summary': """
        Pequeño resumen o descripción del módulo. Se usa como 
        subtítulo en las listas de módulos.""",

    'description': """
        Descripción larga del módulo.
    """,

    'author': "Mi empresa -  Yo mismo",
    'website': "http://www.miempresa.com",

    # Las categorías pueden utilizarse para filtrar los listados de
    # módulos.
    # Mirar https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # para conocer el listado completo de Categorías
    'category': 'Uncategorized',
    'version': '0.1',

    # módulos necesarios para que nuestro módulo funcione correctamente
    'depends': ['board', 'base'],

    # *.xml que se van a cargar cada vez que reiniciemos actualizando
    'data': [
        'views/course_model_view.xml',
        'views/res_partner_view.xml',
        'views/session_model_view.xml',
        'security/groups.xml',
        'security/ir.model.access.csv'
#        'security/security.xml',
#        'views/views.xml',
#        'views/templates.xml',
#        'views/partner.xml',
#        'views/session.xml',
#        'views/wizard.xml',
#        'security/ir.model.access.csv',
#        'reports/reports.xml',
#        'views/session_board.xml',
    ],
    # Sólo se cargaran en modo demo
    'demo': [
        'demo/data.xml',
    ],
}