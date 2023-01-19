# -*- coding: utf-8 -*-
{
    'name': "Eurosense Custo",

    'summary': """
        All Eurosense customization
        """,

    'description': """
        All Eurosense customization
    """,

    'category': 'customization',

    'depends': ['base', 'hr', 'hr_timesheet'],

    'data': [
        'security/groups.xml',
        'security/record_rules.xml',

        'views/hr_employee_views.xml',
        'views/hr_timesheets_views.xml',
    ],

    'license': 'LGPL-3',
}
