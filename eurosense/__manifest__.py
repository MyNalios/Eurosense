# -*- coding: utf-8 -*-
{
    'name': "eurosense",

    'summary': """
        Eurosense""",

    'description': """
        Eurosense
    """,

    'author': "istarii",
    'website': "https://istarii.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'ERP',
    'version': '14.0.0.7',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_accountant', 'contacts'],

    # always loaded 
    'data': [
        'security/eurosense_security.xml',
        'security/ir.model.access.csv',
        'views/partner.xml',
        'views/user.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'auto_install': True,
}
