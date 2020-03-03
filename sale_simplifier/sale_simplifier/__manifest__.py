{
    'name': "sale_simplifier",
    'summary': """
        develop for monopark
        """,
    'description': """
        
    """,
    'author': "xmarts",
    'website': "http://www.xmarts.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '12.0.1',
    # any module necessary for this one to work correctly
    'depends': ['sale'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}