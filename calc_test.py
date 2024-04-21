import unittest
from calc import Calc

class JakakolwiekKlasaTestowa(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(40, self.calc.add(10,30))

if __name__ == '__main__':
    unittest.main()