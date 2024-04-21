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

    def test_odejmowania(self):
        self.assertEqual(10, self.kalkulator.odejmij(-10,-20))
        self.assertEqual(-10, self.kalkulator.odejmij(10,20))
        self.assertEqual(-30, self.kalkulator.odejmij(-10,20))
        self.assertEqual(-10, self.kalkulator.odejmij(-10,0))

    def test_mnozenia(self):
        self.assertEqual(6,self.kalkulator.pomnoz(2,3))
        self.assertEqual(6,self.kalkulator.pomnoz(-2,-3))
        self.assertEqual(-6,self.kalkulator.pomnoz(2,-3))
        self.assertEqual(0,self.kalkulator.pomnoz(2,0))

    def test_dzielenia(self):
        self.assertEqual(1.5, self.kalkulator.podziel(3,2))
        self.assertEqual(2, self.kalkulator.podziel(-4,-2))
        self.assertEqual(-2.5, self.kalkulator.podziel(-5,2))
        self.assertEqual(0, self.kalkulator.podziel(0,2))

    def test_dzielenia_przez_zero(self):
        self.assertEqual("Nie dzieli się przez zero!", self.kalkulator.podziel(4,0))


if __name__ == '__main__':
    unittest.main()