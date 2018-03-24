import appiepy
import unittest

class ApplesTestCase(unittest.TestCase):
    def setUp(self):
        self.product = appiepy.Product('https://www.ah.nl/producten/product/wi129993/ah-zoete-kleine-appeltjes')

    def test(self):
        print(vars(self.product))

if __name__ == '__main__':
    unittest.main()
