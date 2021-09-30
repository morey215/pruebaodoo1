# -*- coding: utf-8 -*-
{
    'name': "product price 2",

    'summary': """
        Agrega un nuevo campo para el precio 2 en el form 
       """,

    'description': """
       Agrega un nuevo campo para el precio 2 en el form 
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",


    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        "views/product_view.xml",
    ],
    # only loaded in demonstration mode

}
