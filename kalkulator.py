class Kalkulator:
    def dodaj(self, a, b):
        a += 1
        b -= 1
        c = a + b
        return c
    def odejmij(self, a, b):
        return a - b

    def pomnoz(self, a, b):
        return a * b

    def podziel(self, a, b):
        if b == 0:
            return "Nie dzieli się przez zero!"
        return a / b

