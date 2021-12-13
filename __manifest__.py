# -*- coding: utf-8 -*-
{
    'name': 'Sequential Number for Barcode',

    'summary': 'Adds Product Group Field and uses that to auto generate barcode number',

    'description': '''
        Task ID: 2682681
        Add product group field to product.template
        Use the first two digits to generate barcode number for product
    ''',

    'license': 'OPL-1',

    'author': 'Odoo Inc',

    'website': 'https://www.odoo.com',

    'category': 'custom',

    'version': '0.1',

    'depends': ['product'],

    'data': [
        'views/product_view_inherit.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False
}