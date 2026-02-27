{
    'name': 'Mini Sales Approval',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Sales Order tasdiqlash jarayonini boshqarish',
    'author': 'Your Name',
    'depends': ['sale_management', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'data/sequence.xml',
        'views/sale_approval_views.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}