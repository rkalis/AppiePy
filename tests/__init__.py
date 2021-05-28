import appiepy
import unittest
from pprint import pprint

class ProductTests(unittest.TestCase):
    def test_url_path(self):
        # given
        url = '/producten/product/wi395948/ah-kleintje-spinazie'

        # when
        product = appiepy.Product(url)

        # then
        self.assertEqual(product.url, url)
        self.assertIsInstance(product.id, str)
        self.assertIsInstance(product.brand, str)
        self.assertIsInstance(product.image_url, str)
        self.assertIsInstance(product.description, str)
        self.assertIsInstance(product.summary, str)
        self.assertIsInstance(product.unit_size, str)
        self.assertIsInstance(product.category, str)
        self.assertIsInstance(product.is_available, bool)
        self.assertIsInstance(product.price_current, float)
        self.assertIsInstance(product.is_discounted, bool)
        self.assertIsInstance(product.features, list)
        self.assertIsInstance(product.nutrition, dict)

    def test_full_url(self):
        # given
        url = 'https://www.ah.nl/producten/product/wi395948/ah-kleintje-spinazie'

        # when
        product = appiepy.Product(url)

        # then
        self.assertEqual(product.url, url)
        self.assertIsInstance(product.id, str)
        self.assertIsInstance(product.brand, str)
        self.assertIsInstance(product.image_url, str)
        self.assertIsInstance(product.description, str)
        self.assertIsInstance(product.summary, str)
        self.assertIsInstance(product.unit_size, str)
        self.assertIsInstance(product.category, str)
        self.assertIsInstance(product.is_available, bool)
        self.assertIsInstance(product.price_current, float)
        self.assertIsInstance(product.is_discounted, bool)
        self.assertIsInstance(product.features, list)
        self.assertIsInstance(product.nutrition, dict)

    def test_ingredients_parsed(self):
        # given
        url = '/producten/product/wi193679/lay-s-paprika'

        # when
        product = appiepy.Product(url)

        # then
        self.assertIsInstance(product.ingredients, list)

    def test_allergy_parsed(self):
        # given
        url = '/producten/product/wi33693/ah-halfvolle-melk'

        # when
        product = appiepy.Product(url)

        # then
        self.assertIsInstance(product.allergy, list)

    def test_nutrition_parsed(self):
        # given
        url = '/producten/product/wi496941/princes-tonijnstukken-in-water'

        # when
        product = appiepy.Product(url)

        # then
        self.assertIsInstance(product.nutrition, dict)

    def test_nonexisting_product(self):
        # given
        url = '/producten/product/wi193679/'

        # then
        with self.assertRaises(appiepy.ProductNotFoundException) as context:
            # when
            product = appiepy.Product(url)


if __name__ == '__main__':
    unittest.main()
