"""
ZADANIE C3: 
Liczby pierwsze - wyścig algorytmów
Porównanie wydajności generowania liczb pierwszych metodą tradycyjną
oraz Sitem Eratostenesa.

ALGORYTMY:
1. Metoda tradycyjna-brute force: Sprawdzanie dzielników każdego kandydata do sqrt(k).
2. Sito Eratostenesa: Wykreślanie wielokrotności liczb w tablicy.

WYMAGANIA:
- Pomiar czasu z użyciem modułu time.
- Obsługa błędów.
"""

import math
import time

def timer_decorator(func, *args):
    """Mierzy czas wykonania przekazanej funkcji."""
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    duration = end_time - start_time
    return result, duration

def get_primes_traditional(limit):
    """
    Znajduje liczby pierwsze metodą dzielenia.
    """
    primes = []
    if limit < 2:
        return primes
    
    # Sprawdzamy każdą liczbę od 2 do limit
    for num in range(2, limit + 1):
        is_prime = True
        # Optymalizacja: sprawdzamy dzielniki tylko do pierwiastka z num
        for div in range(2, int(math.sqrt(num)) + 1):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def get_primes_sieve(limit):
    """
    Znajduje liczby pierwsze Sitem Eratostenesa.
    """
    if limit < 2:
        return []

    # Inicjalizacja tablicy prawdy (True = liczba jest pierwsza)
    # Indeksy odpowiadają liczbom.
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 i 1 nie są pierwsze

    for current_num in range(2, int(math.sqrt(limit)) + 1):
        if sieve[current_num]:
            # Wykreśl wielokrotności current_num, zaczynając od jego kwadratu
            # (mniejsze wielokrotności zostały już wykreślone przez mniejsze liczby)
            for multiple in range(current_num * current_num, limit + 1, current_num):
                sieve[multiple] = False
    
    # Konwersja tablicy boolowskiej na listę liczb
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

def main():
    print("--- Zadanie C3: Porównanie wydajności algorytmów ---")
    
    while True:
        try:
            user_input = input("\nPodaj górny zakres poszukiwań (N) lub 'exit': ").strip()
            
            if user_input.lower() == 'exit':
                break
                
            n = int(user_input)
            
            if n < 2:
                print("Zakres musi być większy lub równy 2.")
                continue
            
            print(f"\nStartuje wyścig dla N = {n}...")
            
            # Metoda tradycyjna
            print("1. Metoda tradycyjna:  Przetwarzanie...", end="\r")
            primes_trad, time_trad = timer_decorator(get_primes_traditional, n)
            print(f"1. Metoda tradycyjna:  {time_trad:.6f} sek. (Znaleziono: {len(primes_trad)})")

            # Sito Eratostenesa
            print("2. Sito Eratostenesa:  Przetwarzanie...", end="\r")
            primes_sieve, time_sieve = timer_decorator(get_primes_sieve, n)
            print(f"2. Sito Eratostenesa:  {time_sieve:.6f} sek. (Znaleziono: {len(primes_sieve)})")

            # Weryfikacja i wnioski
            if primes_trad == primes_sieve:
                print("Status: WYNIKI ZGODNE (poprawność algorytmów potwierdzona).")
            else:
                print("BŁĄD KRYTYCZNY: Wyniki algorytmów są różne!")
            
            if time_sieve > 0:
                speedup = time_trad / time_sieve
                print(f"Wniosek: Sito było {speedup:.2f}x szybsze.")
            
        except ValueError:
            print("Błąd: Wprowadź liczbę całkowitą.")
        except Exception as e:
            print(f"Nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    main()