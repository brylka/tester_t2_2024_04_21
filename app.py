from kalkulator import Kalkulator

def main():
    print("Kalkulator")

    while True:
        print("Wybierz operację:\n1. Dodaj\n2. Odejmij\n3. Pomnóż\n4. Podziel\n5. Koniec")

        wybor = input("Wybierz opcję (1/2/3/4/5): ")

        if wybor == "5":
            print("Dziękuję za użycie kalkulatora...")
            break

        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        kalkulator = Kalkulator()

        try:
            if wybor == "1":
                print("Wynik dodawania: ", kalkulator.dodaj(liczba1, liczba2))
            elif wybor == "2":
                print("Wynik odejmowania: ", kalkulator.odejmij(liczba1, liczba2))
            elif wybor == "3":
                print("Wynik mnożenia: ", kalkulator.pomnoz(liczba1, liczba2))
            elif wybor == "4":
                print("Wynik dzielenia: ", kalkulator.podziel(liczba1, liczba2))
            else:
                print("Nieprawidłowa opcja. Wybierz inną.")
        except Exception as exception:
            print(exception)

if __name__=="__main__":
    main()