# -----------------------------------------------------------------------------
#
#    Copyright (C) 2021  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'tronic',
    'version': '11.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customization for TRONIC',
    "development_status": "Beta",  # "Alpha|Beta|Production/Stable|Mature"
    'author': 'Tronic Software',
    'depends': [
        # basic applications
        'sale_management',
        'account_invoicing',
        'purchase',
        'stock',

        # minimum modules for argentinian localizacion + utilities + fixes
        'standard_depends_ce',

        # utilitarios adicionales
        'backend_theme_v11',

        # requerido por la restriccion de menuitems
        #'mail', 'calendar', 'contacts', 'mrp', 'sale', 'purchase', 'stock',
        #'account', 'hr', 'base'
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'config': [
    ],

    'env-ver': '2',
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8069',

    'git-repos': [
        'https://github.com/pabarrientos/cl-tronic.git',
        'https://github.com/jobiols/odoo-addons.git',
        'https://github.com/jobiols/rafi16jan-backend-theme.git',
        'https://github.com/jobiols/odoo-jeo-ce.git',

        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/account-payment.git',
        'https://github.com/ingadhoc/website.git',
        'https://github.com/ingadhoc/miscellaneous.git',
        'https://github.com/ingadhoc/argentina-reporting.git',
        'https://github.com/ingadhoc/reporting-engine.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/sale.git',
        'https://github.com/ingadhoc/odoo-support.git',
        'https://github.com/ingadhoc/product.git',
        'https://github.com/ingadhoc/partner.git',
        'https://github.com/ingadhoc/account-invoicing.git',
        'https://github.com/ingadhoc/stock.git',

        'https://github.com/oca/partner-contact.git',
        'https://github.com/oca/web.git',
        'https://github.com/oca/server-tools.git',
        'https://github.com/oca/social.git',
        'https://github.com/oca/server-brand.git',
        'https://github.com/oca/server-ux.git',
        'https://github.com/oca/project.git',
        'https://github.com/oca/queue.git',
    ],

    'docker-images': [
        'odoo jobiols/odoo-jeo:11.0',
        'postgres postgres:11.1-alpine',
        'nginx nginx',
        'aeroo adhoc/aeroo-docs'
    ]

}
