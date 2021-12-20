# -*- coding: utf-8 -*-
{
    'name': 'Sales order lines to Manufacturing order link. Credit Limit Notification',

    'summary': 'Add buttons to navigate between SOL and MO',

    'description': '''
        Task ID: 2682630

        Section 1
            A.Create a link on the Manufacturing order (mrp.production) to Sales Order Lines (sale.order.line)
            B. Show the description of the sale order line on the manufacturing order

        Section 2.
            Link the production orders to the associated sales order with a magic button.
            Essentially if the Sales Order contains 3 Sale Order Line items that all create a Manufacturing Order, the Sales Order should show a magic button which says “3 Manufacturing Orders” linked with the Manufacturing Order’s created by the Sales Order Lines.
            And when clicked on that button, takes us to the list view of the associated MOs with that SO.

        Section 3. 
            Custom field on the Sales Order Lines needed for the MO 
            Populate the field x_studio_custom_notes on Manufacturing order form (mrp.production form.)
            Custom notes info: to pull from x_studio_custom_notes (Custom notes) field on related sale.order.line

        Section 4
            Moved from task 2194652
            On the SO sale.order model, we bring in the credit limit and total due amount of the res.partner, and compare it.
            1. If total due > credit limit, we will display a text warning on the top of the sale order (not a pop-up) that mentions “Customer is past credit limit. Please check with administrator to confirm this sales order”
            2. If point 1 is true, hide the confirm button the SO level for all groups except Administrator/Settings and Sales/Administrator.
            3. Have a checkbox named ‘SO on hold’ and set as true if condition in point 1 is matched.
            4. If a payment is received for that customer after a credit hold was placed for that customer, we need to revoke the credit hold and ensure the confirm button can reappear as before and also set the ‘SO on hold’ checkbox as false.
    ''',

    'license': 'OPL-1',

    'author': 'Odoo Inc',

    'website': 'https://www.odoo.com',

    'category': 'custom',

    'version': '0.1',

    'depends': ['mrp', 'sale'],

    'data': [
        'views/mrp_production.xml',
        'views/sale_order.xml'
    ],

    'installable': True,
    'application': False,
    'auto_install': False
}