import sys

# Zwiększamy limit rekurencji dla bezpieczeństwa, choć przy intach rzadko potrzebne
sys.setrecursionlimit(2000)

def nwd(a, b):
    """
    Algorytm Euklidesa do znalezienia Największego Wspólnego Dzielnika.
    Potrzebne, żeby sprawdzić, czy liczby są względnie pierwsze.
    """
    while b:
        a, b = b, a % b
    return a

def rozwiaz_rekurencyjnie(licznik, mianownik, wynik_lista):
    """
    Funkcja rekurencyjna wyznaczająca kolejne współczynniki a0, a1...
    Zasada: odwracamy ułamek (mianownik/licznik), wyciągamy całość,
    a resztę wrzucamy do kolejnego wywołania.
    """
    # Warunek stopu: jeśli licznik to 0, kończymy
    if licznik == 0:
        return

    # Obliczamy część całkowitą z odwróconego ułamka (mianownik // licznik)
    czesc_calkowita = mianownik // licznik
    wynik_lista.append(czesc_calkowita)
    
    # Obliczamy nową resztę (nowy licznik dla następnego kroku)
    nowa_reszta = mianownik % licznik
    
    # Wywołanie rekurencyjne:
    # Stary licznik staje się nowym mianownikiem
    rozwiaz_rekurencyjnie(nowa_reszta, licznik, wynik_lista)

def main():
    print("--- Zadanie Z4: Ułamki łańcuchowe ---")
    
    try:
        # Pobranie danych od użytkownika
        # l = licznik, m = mianownik
        l_str = input("Podaj licznik (l): ")
        m_str = input("Podaj mianownik (m): ")
        
        l = int(l_str)
        m = int(m_str)
        
        # Walidacja 1: Czy liczby dodatnie
        if l <= 0 or m <= 0:
            print("Błąd: Liczby muszą być naturalne dodatnie.")
            return

        # Walidacja 2: Czy liczby są względnie pierwsze 
        wspolny_dzielnik = nwd(l, m)
        if wspolny_dzielnik != 1:
            print(f"Błąd: Liczby {l} i {m} nie są względnie pierwsze.")
            print(f"Ich wspólny dzielnik to: {wspolny_dzielnik}. Skróć ułamek i spróbuj ponownie.")
            return

        print(f"\nRozkładam ułamek {l}/{m}...")
        
        # Lista na wyniki
        wspolczynniki = []
        
        # Uruchomienie rekurencji
        rozwiaz_rekurencyjnie(l, m, wspolczynniki)
        
        # Wyświetlenie wyniku
        print(f"Współczynniki (a0, a1, ... an): {wspolczynniki}")
        
        # Opcjonalnie: ładny format wzoru
        print("Reprezentacja: [", end="")
        print(", ".join(str(x) for x in wspolczynniki), end="")
        print("]")

    except ValueError:
        print("Błąd: Wprowadzono niepoprawne dane.")
    except RecursionError:
        print("Błąd: Zbyt głęboka rekurencja (bardzo duże liczby).")

    input("\nNaciśnij Enter, aby zakończyć.")

if __name__ == "__main__":
    main()