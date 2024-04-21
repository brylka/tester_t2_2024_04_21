import unittest


class Kalkulator:
    def dodaj(self, a, b):
        return a + b


class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_dodawania(self):
        self.assertEqual(30, self.kalkulator.dodaj(10, 20))


if __name__ == '__main__':
    unittest.main()