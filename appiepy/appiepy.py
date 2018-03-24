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

class Product():
    def __init__(self, url):
        self.url = url

        request_url = _get_request_url(url)
        res = requests.get(request_url).json()

        for lane in res['_embedded']['lanes']:
            if lane['type'] == 'ProductDetailLane':
                for item in lane['_embedded']['items']:
                    if item['type'] != 'Product':
                        continue
                    product = item['_embedded']['product']
                    self.id = product['id']
                    self.brand = product['brandName']
                    self.description = product['description'].replace('\xad', '')
                    self.summary = product['details']['summary']
                    self.unit_size = product['unitSize']
                    self.category = product['categoryName']
                    self.is_available = product['availability']['orderable']
                    self.price = product['priceLabel']
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
