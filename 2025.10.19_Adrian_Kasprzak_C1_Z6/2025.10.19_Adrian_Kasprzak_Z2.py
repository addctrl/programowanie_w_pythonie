def czy_pierwsza(n):
    """
    Funkcja pomocnicza sprawdzająca, czy liczba n jest pierwsza.
    """
    if n < 2:
        return False
    # Sprawdzamy dzielniki od 2 do pierwiastka z n
    # int(n**0.5) to pierwiastek
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def czy_beta_super_pierwsza(n):
    """
    Główna logika zadania Z2.
    1. Sprawdza czy n jest pierwsza.
    2. Zamienia na binarny, sumuje cyfry (liczy jedynki) i sprawdza czy suma jest pierwsza.
    """
    # Warunek 1: Sama liczba musi być pierwsza
    if not czy_pierwsza(n):
        return False
    
    # Warunek 2: Suma cyfr w zapisie binarnym musi być pierwsza
    # bin(n) zwraca np. '0b1011', ucinamy '0b' przez [2:]
    napis_binarny = bin(n)[2:]
    
    # W systemie binarnym są tylko 0 i 1. Suma cyfr to po prostu liczba jedynek.
    # Przykład: dla 11 (1011) suma to 3.
    suma_cyfr = napis_binarny.count('1')
    
    # Sprawdzamy czy ta suma jest liczbą pierwszą
    if czy_pierwsza(suma_cyfr):
        return True
        
    return False

def main():
    print("--- Zadanie Z2: Sprawdzanie liczb beta-super-pierwszych ---")
    
    # Testujemy zakres liczb (np. od 0 do 100) żeby pokazać działanie
    print("Szukanie liczb beta-super-pierwszych w zakresie 0-100:")
    
    znalezione = 0
    for liczba in range(101):
        if czy_beta_super_pierwsza(liczba):
            # Pokazujemy detale dla potwierdzenia
            binarnie = bin(liczba)[2:]
            suma = binarnie.count('1')
            print(f"Znaleziono: {liczba} (Binarnie: {binarnie}, Suma cyfr: {suma})")
            znalezione += 1
            
    print("-" * 30)
    print(f"Łącznie znaleziono: {znalezione}")

    # Sprawdzenie ręczne (interaktywne)
    try:
        wejscie = input("\nPodaj liczbę do sprawdzenia (lub Enter by zakończyć): ")
        if wejscie:
            liczba_uzytkownika = int(wejscie)
            if czy_beta_super_pierwsza(liczba_uzytkownika):
                print(f"TAK! {liczba_uzytkownika} to liczba beta-super-pierwsza.")
            else:
                print(f"NIE. {liczba_uzytkownika} nie spełnia warunków.")
    except ValueError:
        print("To nie jest poprawna liczba.")

if __name__ == "__main__":
    main()