"""
ZADANIE C4 :
Napisz rekurencyjnie cztery funkcje, które generują następujące ciągi 
n-elementowe:
    a. (3; 6; 9; 12; 15; 18; 21; 24...)
    b. (8; -4; 2; -1; 0,5; -0,25; 0,125...)
    c. (2; 6; 3; 7; 4; 8; 5; 9; 6; 10; 7; 11...)
    d. (1; 2; -4; -3; -1; -5; -8; -9; -14...)
(liczbę n podaje użytkownik).
Ad. 
Zamiast skupić się na samej rekurencji, użyłem dekoratora @lru_cache, który
zapamiętuje wyniki funkcji i nie powtarza ich obliczeń. Chciałem znaleźć sposób na 
optymalizację złozoności algorytmu rekurencyjnego wykorzystując do tego wbudowane 
moduły Pythona. 
"""

import sys
from functools import lru_cache

# Zwiększenie limitu rekurencji
sys.setrecursionlimit(2000)

# Dekorator @lru_cache sprawia, że Python zapamiętuje wyniki funkcji.
# maxsize=None oznacza, że zapamiętujemy wszystko (bez limitu pamięci).

@lru_cache(maxsize=None)
def sequence_a(n):
    # a(n) = a(n-1) + 3
    if n == 1:
        return 3
    return sequence_a(n - 1) + 3

@lru_cache(maxsize=None)
def sequence_b(n):
    # b(n) = b(n-1) * -0.5
    if n == 1:
        return 8
    return sequence_b(n - 1) * -0.5

@lru_cache(maxsize=None)
def sequence_c(n):
    # Ciąg naprzemienny
    if n == 1:
        return 2
    
    if n % 2 == 0:
        return sequence_c(n - 1) + 4
    else:
        return sequence_c(n - 1) - 3

@lru_cache(maxsize=None)
def sequence_d(n):
    # d(n) = d(n-1) + d(n-3)
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return -4
    
    return sequence_d(n - 1) + sequence_d(n - 3)

def main():
    print("--- Generowanie ciągów (Optimized Recursion) ---")
    
    try:
        n = int(input("Podaj liczbę wyrazów (n): "))
        if n <= 0:
            print("Liczba n musi byc dodatnia.")
            return
    except ValueError:
        print("Błąd: n musi być liczbą całkowitą.")
        return

    # Dzięki cache, gdy pętla idzie od 1 do n, każde kolejne wywołanie
    # korzysta z wyniku poprzedniego obliczonego w poprzedniej iteracji.
    # Koszt obliczeń spada drastycznie.
    
    print("\nCiąg A:")
    print([sequence_a(i) for i in range(1, n + 1)])

    print("\nCiąg B:")
    print([sequence_b(i) for i in range(1, n + 1)])

    print("\nCiąg C:")
    print([sequence_c(i) for i in range(1, n + 1)])

    print("\nCiąg D:")
    print([sequence_d(i) for i in range(1, n + 1)])
    
    # Wyświetlenie statystyk cache 
    # Ciekawostka, nie jest częścią zadania, ale zaciekawiła mnie próba optymalizacji rekurencji 
    # misses - dowód złozoności liniowej algorytmu, tyle wykonań ile liczb wygenerowanych
    # hits - ile razy wywołano już wcześniej, ale był zapisany wynik, więc funkcja nie wykonała się ponownie
    # maxsize - pojemność magazynu, nie był ograniczany
    # currsize - aktualna ilość elementów w magazynie (RAM)
    print(sequence_d.cache_info()) 

    input("\nAby zakończyć program, naciśnij klawisz Enter.")

if __name__ == "__main__":
    main()