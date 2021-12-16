# -*- coding: utf-8 -*-
{
    'name': 'OWL Framework: POS changes',

    'summary': 'Add customer type field to frontend and backend',

    'description': '''
        Task ID: 2682649
        Add selection field named Customer type on pos client screen.
        1.1) add the same field on the partner form view on the odoo backend.
        1.2) Field should populate selected value in the backed and pos visa-versa.
    ''',

    'license': 'OPL-1',

    'author': 'Odoo Inc',

    'website': 'https://www.odoo.com',

    'category': 'custom',

    'version': '0.1',

    'depends': ['point_of_sale'],

    'data': [
        'views/pos_assets.xml',
        'views/res_partner_view.xml'
    ],

    'qweb': ['static/src/xml/ClientDetailsEdit.xml'],

    'installable': True,
    'application': False,
    'auto_install': False
}