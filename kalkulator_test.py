import unittest
from kalkulator import Kalkulator

class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_dodawania(self):
        self.assertEqual(30, self.kalkulator.dodaj(10,20))
        self.assertEqual(-177, self.kalkulator.dodaj(-123,-54))
        self.assertEqual(-10, self.kalkulator.dodaj(10,-20))
        self.assertEqual(-10, self.kalkulator.dodaj(-10,0))

if __name__ == '__main__':
    unittest.main()