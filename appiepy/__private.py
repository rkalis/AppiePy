import requests as requests
from urllib.parse import urlparse as urlparse
from xml.etree import ElementTree as ElementTree

def _get_request_url(product_url):
    path = urlparse(product_url).path
    request_url = 'https://www.ah.nl/service/rest/delegate?url={}'.format(path)
    return request_url

def _parse_nutrition(string):
    string = string.split('[/table]')[0] + '[/table]'
    string = string.replace('[', '<').replace(']', '>')
    table = ElementTree.XML(string)[1:]
    nutrition = {}
    for row in table:
        nutrition[row[0].text] = row[1].text
    return nutrition

def _split(s):
    parts = []
    bracket_level = 0
    current = []
    for c in (s + ","):
        if c == "," and bracket_level == 0:
            parts.append("".join(current))
            current = []
        else:
            if c in ["{", "(", "["]:
                bracket_level += 1
            elif c in ["}", ")", "]"]:
                bracket_level -= 1
            current.append(c)
    return parts

def _parse_ingredients(string):
    return _split(string.replace('Ingrediënten: ', ''))

class Product():
    def __init__(self, url):
        self.url = url

        request_url = _get_request_url(url)
        res = requests.get(request_url)
        if not res.ok:
            raise ProductNotFoundException(url)
        res = res.json()

        for lane in res['_embedded']['lanes']:
            if lane['type'] == 'ProductDetailLane':
                for item in lane['_embedded']['items']:
                    if item['type'] != 'Product':
                        continue
                    product = item['_embedded']['product']
                    self.id = product.get('id', None)
                    self.brand = product.get('brandName', None)
                    if product.get('images'):
                        self.image_url = product['images'][0]['link'].get('href', None)
                    else:
                        self.image_url = None
                    self.description = product.get('description', '').replace('\xad', '')
                    self.summary = product.get('details', {}).get('summary', None)
                    self.unit_size = product.get('unitSize', None)
                    self.category = product.get('categoryName', None)
                    self.is_available = product.get('availability', {}).get('orderable', False)
                    priceLabel = product.get('priceLabel', {})
                    self.price_current = priceLabel.get('now', None)
                    self.price_previous = priceLabel.get('was', None)
                    self.is_discounted = 'discount' in product
            elif lane['type'] == 'StoryLane':
                for item in lane['_embedded']['items']:
                    for section in item['_embedded']['sections']:
                        for content in section['_embedded']['content']:
                            if 'features' in content:
                                self.features = content['features']
                            if 'text' in content and \
                               'body' in content['text'] and \
                               'Eiwitten' in content['text']['body']:
                                self.nutrition = _parse_nutrition(content['text']['body'])
                            if 'text' in content and \
                               'body' in content['text'] and \
                               'Ingrediënten:' in content['text']['body']:
                                self.ingredients = _parse_ingredients(content['text']['body'])


class ProductNotFoundException(Exception):
    def __init__(self, url):
        Exception.__init__(self, "Product with URL {} could not be found".format(url))
        self.url = url
