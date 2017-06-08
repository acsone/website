#"-*- coding: utf-8 -*-
# © 2015-2017 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Website Dynamic Snippet",
    'summary': """
        This module provides abstract models and views used to develop
        dynamic snippets.""",
    'author': 'ACSONE SA/NV',
    'website': "http://acsone.eu, "
               "Odoo Community Association (OCA)",
    'category': 'Website',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'website',
        'web_editor',
        'website_parameterized_snippet',
    ],
    'data': [
        'views/website_dynamic_snippet.xml',
    ],
}
