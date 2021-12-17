# -*- coding: utf-8 -*-
{
    'name': 'Limit available Products in Shop based on O-2-Many Field on Contact Form',

    'summary': 'Limit visibility of products to only specified contacts',

    'description': '''
        Create O-2-Many Field on Contact Form View, where we can select multiple products. These will be only products this contact should be able to see on the Shop.
        Public Users should not have access to the Shop, unless invited to join the Customer Portal.
    ''',

    'license': 'OPL-1',

    'author': 'Odoo Inc',

    'website': 'https://www.odoo.com',

    'category': 'custom',

    'version': '0.1',

    'depends': ['product'],

    'data': [
        'views/contact_view.xml',
        'views/product_view.xml',
    ],
}