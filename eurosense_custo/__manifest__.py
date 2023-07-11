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

    'depends': ['base', 'hr', 'hr_timesheet', 'hr_recruitment'],

    'data': [
        'security/groups.xml',
        'security/record_rules.xml',
        'security/ir.model.access.csv',

        'views/hr_employee_views.xml',
        'views/hr_timesheets_views.xml',
        'views/hr_job_views.xml',
    ],

    'license': 'LGPL-3',
}
