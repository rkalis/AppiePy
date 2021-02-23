# AppiePy: A Python API for Albert Heijn

[![PyPI - Version](https://img.shields.io/pypi/v/appiepy.svg)](https://pypi.python.org/pypi/appiepy/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/appiepy)](https://pypi.python.org/pypi/appiepy/)
[![PyPI - License](https://img.shields.io/pypi/l/appiepy.svg)](https://pypi.python.org/pypi/appiepy/)

AppiePy is a wrapper around Albert Heijn products you can find on their website [https://ah.nl/](https://ah.nl/).
It allows you to retrieve information about these products and use it inside your application. Common uses are price/discount information, brand/category information, or nutritional information.

## Installation
Installation can be done through pip:

```shell
pip install appiepy
```

## Usage

```python
from appiepy import Product
import json

# Full product url
product = Product('https://www.ah.nl/producten/product/wi193679/lay-s-paprika')

# Or just the path
product = Product('/producten/product/wi193679/lay-s-paprika')

print(json.dumps(product.__dict__, indent=4, sort_keys=True))

# {
#     "allergy": ["melk", "glutenbevattende granen", "tarwe"],
#     "brand": "Lay's",
#     "category": "Snoep, koek, chips en chocolade/Paprika chips",
#     "description": "Lay's Paprika",
#     "features": [
#         { "identifier": "green_dot", "text": "Groene Punt" },
#         { "identifier": "recyclable_general_claim", "text": "Recyclebaar" }
#     ],
#     "id": "wi193679",
#     "image_url": "https://static.ah.nl/static/product/AHI_43545239373137323733_1_LowRes_JPG.JPG",
#     "ingredients": [
#         "aardappelen",
#         "plantaardige oli\u00ebn (zonnebloem, koolzaad, ma\u00efs, in wisselende hoeveelheden)",
#         "paprikasmaak [suiker, zout, paneermeel (van [b]TARWE[/b]), paprika, [b]MELKWEI[/b]-permeaat, uienpoeder, kaliumchloride, aroma's, knoflookpoeder, johannesbroodpitmeel, kleurstof (paprika-extract), rookaroma's, voedingszuren (citroenzuur en appelzuur)]"
#     ],
#     "is_available": true,
#     "is_discounted": false,
#     "nutrition": {
#         "Eiwitten": "6.4 g",
#         "Energie": "2244 kJ (538 kcal)",
#         "Koolhydraten": "54 g",
#         "Vet": "32 g",
#         "Voedingsvezel": "4.8 g",
#         "Waarvan suikers": "2.7 g",
#         "Waarvan verzadigd": "3.9 g",
#         "Zout": "1.2 g"
#     },
#     "price_current": 1.49,
#     "price_previous": null,
#     "summary": "De enige echte Lay's chips met paprikasmaak[list][*]Zonder kunstmatige kleurstoffen en conserveringsmiddelen\n[*]Zonder toegevoegde smaakversterkers\n[*]Bevat 7-8 porties\n[/list]",
#     "unit_size": "225 g",
#     "url": "/producten/product/wi193679/lay-s-paprika"
# }
```

## Command Line Usage
```shell
python3 -m appiepy /producten/product/wi193679/lay-s-paprika
```

This logs a JSON representation of the product, similar to the logged output above.
