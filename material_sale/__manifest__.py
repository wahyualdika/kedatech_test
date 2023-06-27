{
    "name": "Material Sale",
    "summary": "Material Sale",
    "version": "15.0.1.0.0",
    "author": "Wahyu Alif Aldika",
    "category": "Sale",
    "license": "AGPL-3",
    'depends': [
        'base','account','sale','purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/material_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    "installable": True,
}
