AppiePy: A Python API for Albert Heijn
======================================

.. image:: https://img.shields.io/pypi/v/appiepy.svg
      :target: https://pypi.python.org/pypi/appiepy/
      :alt: Version
.. image:: https://img.shields.io/pypi/l/appiepy.svg
      :target: https://pypi.python.org/pypi/appiepy/
      :alt: PyPI - License

AppiePy is a wrapper around Albert Heijn products you can find on their website `https://ah.nl/ <https://ah.nl/>`_.
It allows you to retrieve information about these products and use it inside your application. Common uses are price/discount information, brand/category information, or nutritional information.


Installation
------------
Installation can be done through pip:

.. code-block:: shell

    pip install appiepy

Usage
-----

.. code-block:: python

    from appiepy import Product
    from pprint import pprint

    # Full product url
    product = Product('https://www.ah.nl/producten/product/wi193679/lay-s-paprika')

    # Or just the path
    product = Product('/producten/product/wi193679/lay-s-paprika')

    pprint(vars(products))

    # {
    #     'brand': "Lay's",
    #     'category': 'Snoep, koek, chips/Paprika chips',
    #     'description': "Lay's Paprika",
    #     'features': [{'identifier': 'green_dot', 'text': 'Groene Punt'}],
    #     'id': 'wi193679',
    #     'ingredients': ['aardappelen',
    #                     ' plantaardige oliën (zonnebloem (26%), koolzaad (6%))',
    #                     ' paprikasmaak [suiker, zout, paneermeel (van TARWE), '
    #                     'paprika, MELKWEI-permeaat, uienpoeder, kaliumchloride, '
    #                     "aroma's, knoflookpoeder, johannesbroodpitmeel, kleurstof "
    #                     "(paprika-extract), rookaroma's, zuurteregelaars (citroenzuur "
    #                     'en appelzuur)].'],
    #     'is_available': True,
    #     'is_discounted': False,
    #     'nutrition': {'Eiwitten': '6.1 g',
    #                   'Energie': '2215 kJ (531 kcal)',
    #                   'Koolhydraten': '52 g',
    #                   'Vet': '32 g',
    #                   'Voedingsvezel': '4.6 g',
    #                   'Waarvan suikers': '2.4 g',
    #                   'Waarvan verzadigd': '2.7 g',
    #                   'Zout': '1.4 g'},
    #     'price_current': 1.29,
    #     'price_previous': None,
    #     'summary': "De enige echte Lay's chips met paprikasmaak[list][*]Zonder "
    #             'kunstmatige kleurstoffen en conserveringsmiddelen\n'
    #             '[*]Zonder toegevoegde smaakversterkers\n'
    #             '[*]Bevat 7-8 porties\n'
    #             '[/list]',
    #     'unit_size': '225 g',
    #     'url': '/producten/product/wi193679/lay-s-paprika'
    # }
