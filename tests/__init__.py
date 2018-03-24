import appiepy
import unittest

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
        self.assertIsInstance(product.description, str)
        self.assertIsInstance(product.summary, str)
        self.assertIsInstance(product.unit_size, str)
        self.assertIsInstance(product.category, str)
        self.assertIsInstance(product.is_available, bool)
        self.assertIsInstance(product.price, dict)
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
        self.assertIsInstance(product.description, str)
        self.assertIsInstance(product.summary, str)
        self.assertIsInstance(product.unit_size, str)
        self.assertIsInstance(product.category, str)
        self.assertIsInstance(product.is_available, bool)
        self.assertIsInstance(product.price, dict)
        self.assertIsInstance(product.is_discounted, bool)
        self.assertIsInstance(product.features, list)
        self.assertIsInstance(product.nutrition, dict)

if __name__ == '__main__':
    unittest.main()
