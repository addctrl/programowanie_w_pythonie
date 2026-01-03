"""
ZADANIE C10:
Obliczanie przybliżonej wartości liczby Pi z wykorzystaniem wzoru Newtona.
Program ma ustalić, dla jakiego najmniejszego k otrzymamy przybliżenie
z dokładnością do 9 miejsc po przecinku.

Wzór: pi/2 = sum( k! / (2k+1)!! ) od k=0 do nieskończoności.
Wymagana implementacja rekurencyjna silni podwójnej.
"""

import math
import sys

# Zwiekszenie limitu rekurencji, choć Newton jest szybko zbiezny
sys.setrecursionlimit(2000)

def double_factorial(n):
    """
    Oblicza silnię podwójną (n!!) w sposób rekurencyjny.
    Z treści zadania - wzór:
    n!! = 1 dla n=0 lub n=1
    n!! = n * (n-2)!! dla n >= 2
    """
    if n <= 1:
        return 1
    return n * double_factorial(n - 2)

def calculate_pi_newton():
    target_pi = math.pi
    current_sum = 0.0
    k = 0
    epsilon = 1e-9  # Dokładność do 9 miejsc po przecinku

    print(f"Cel: {target_pi:.9f} (wartość oczekiwana, na bazie biblioteki math)")
    print("-" * 30)

    while True:
        # Obliczenie licznika: k!
        numerator = math.factorial(k)
        
        # Obliczenie mianownika: (2k + 1)!!
        # Wymagana funkcja rekurencyjna
        denominator = double_factorial(2 * k + 1)
        
        # Wzór na wyraz ciągu
        term = numerator / denominator
        current_sum += term
        
        # Przybliżenie Pi to 2 * suma (bo wzór jest na pi/2 - wynika z treśc izadania)
        pi_approx = 2 * current_sum
        
        # Sprawdzenie dokładności
        diff = abs(target_pi - pi_approx)
        
        # Debug co 5 kroków (opcjonalne, testowo czy działa prawidłowo)
        if k % 5 == 0:
             print(f"k={k}: {pi_approx:.9f} (diff: {diff:.2e})")

        if diff < epsilon:
            return k, pi_approx

        k += 1

def main():
    print("--- Zadanie C10: Obliczanie przybliżenia Pi z wykorzystaniem wzoru Newtona ---")
    
    try:
        k_found, pi_val = calculate_pi_newton()
        
        print("-" * 30)
        print("SUKCES!")
        print(f"Osiągnięto wymaganą dokładność dla k = {k_found}")
        print(f"Obliczone Pi: {pi_val:.9f}")
        print(f"Wzorcowe Pi:  {math.pi:.9f}")
        
    except RecursionError:
        print("Błąd: Przekroczono limit rekurencji. Zwiększ sys.setrecursionlimit.")

    input("\nNaciśnij Enter, aby zakończyć.")

if __name__ == "__main__":
    main()