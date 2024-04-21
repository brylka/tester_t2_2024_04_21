import unittest
from kalkulator import Kalkulator

class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_dodawania(self):
        wynik = self.kalkulator.dodaj(10,20)
        self.assertEqual(30, wynik)

if __name__ == '__main__':
    unittest.main()