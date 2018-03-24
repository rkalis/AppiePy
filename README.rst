AppiePy: A Python API for Albert Heijn
================================

.. image:: https://img.shields.io/pypi/v/apppiepy.svg
      :target: https://pypi.python.org/pypi/appiepy/
      :alt: Version
.. image:: https://img.shields.io/pypi/l/appiepy.svg
      :alt: PyPI - License

AppiePy is a wrapper around Albert Heijn products you can find on their website `https://ah.nl/ <https://ah.nl/>`_.
It allows you to retrieve information about these products and use it inside your application. Common uses are price/discount information, brand/category information, or nutritional information.



Installation
------------
Installation can be done through pip:

.. code:: bash

    pip install appiepy

Usage
------

.. code:: python

    from appiepy import Product
    from pprint import pprint

    # Full product url
    product = Product('https://www.ah.nl/producten/product/wi395948/ah-kleintje-spinazie')

    # Or just the path
    product = Product('/producten/product/wi395948/ah-kleintje-spinazie')

    pprint(vars(products))

    # {
    #     'brand': 'AH',
    #     'category': 'Aardappel, groente, fruit/Spinazie (vers)',
    #     'description': 'AH Kleintje spinazie',
    #     'features': [{'identifier': 'gezonde_keuze_klavertje', 'text': 'Gezondere keuze'},
    #                 {'identifier': 'free_from_gluten', 'text': 'Bevat geen gluten'},
    #                 {'identifier': 'free_from_milk', 'text': 'Bevat geen melk'}],
    #     'id': 'wi395948',
    #     'is_available': True,
    #     'is_discounted': True,
    #     'nutrition': {'Eiwitten': '3 g',
    #                   'Energie': '110 kJ (26 kcal)',
    #                   'Koolhydraten': '0.9 g',
    #                   'Vet': '0.6 g',
    #                   'Vitamine B11 / Foliumzuur': '130.9 µg',
    #                   'Voedingsvezel': '2 g',
    #                   'Waarvan enkelvoudig onverzadigd': '0 g',
    #                   'Waarvan meervoudig onverzadigd': '0.5 g',
    #                   'Waarvan suikers': '0 g',
    #                   'Waarvan verzadigd': '0.1 g',
    #                   'Zout': '0 g'},
    #     'price': {'now': 1.29},
    #     'summary': 'Spinazie om te (roer)bakken, voor in de salade, stamppot of in '
    #                'een hartige taart. Met spinazie kun je eindeloos combineren. '
    #                'Extra handig! Deze spinazie is al gewassen en dus direct klaar '
    #                'voor gebruik.\n'
    #                '\n'
    #                '[list][*]Met een zachte smaak\n'
    #                '[*]Je kunt spinazie ook rauw eten door een salade of smoothie\n'
    #                '[*]Gewassen in ijswater\n'
    #                '[/list]',
    #     'unit_size': '200 g',
    #     'url': 'https://www.ah.nl/producten/product/wi395948/ah-kleintje-spinazie'
    # }

