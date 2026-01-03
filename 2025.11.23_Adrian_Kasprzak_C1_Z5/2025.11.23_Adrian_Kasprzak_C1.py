"""

Zadanie C1:
Program rozwiązuje dowolne równanie kwadratowe wprowadzone przez użytkownika (współczynniki a, b, c).
Zapewnia obsługę wyjątków oraz czytelny interfejs.
Wykorzystuje bibliotekę sympy do obliczeń symbolicznych/dokładnych (również zespolonych).
"""

from sympy import symbols, solve, SympifyError, sympify, Symbol
from typing import List

def solve_quadratic_equation() -> None:
    """
    Główna funkcja sterująca interakcją z użytkownikiem i obliczeniami.
    Pobiera dane, waliduje je i wyświetla wynik.
    """
    print("--- ROZWIĄZYWANIE RÓWNANIA KWADRATOWEGO ax^2 + bx + c = 0 ---")
    print("Wpisz współczynniki (liczby lub wyrażenia, np. sqrt(2)).")

    x: Symbol = symbols('x')

    while True:
        try:
            # Krok 1: Pobranie danych
            a_input: str = input("Podaj a: ")
            # Zabezpieczenie przed wyjściem
            if a_input.lower() in ['exit', 'quit', 'wyjscie']:
                print("Zamykam system.")
                break

            b_input: str = input("Podaj b: ")
            c_input: str = input("Podaj c: ")

            # Krok 2: Konwersja i walidacja
            # Używamy sympify, żeby obsłużyć ułamki lub pierwiastki wpisane jako tekst
            a = sympify(a_input)
            b = sympify(b_input)
            c = sympify(c_input)

            # Sprawdzenie czy to faktycznie równanie kwadratowe
            if a == 0:
                print("BŁĄD: To nie jest równanie kwadratowe (a=0). To równanie liniowe.")
                continue

            # Krok 3: Obliczenia
            equation = a * x**2 + b * x + c
            solutions: List = solve(equation, x)

            # Krok 4: Prezentacja wyniku
            print(f"\nRównanie: {a}*x^2 + {b}*x + {c} = 0")
            
            if not solutions:
                print("Wynik: Brak rozwiązań.")
            elif len(solutions) == 1:
                print(f"Wynik (jedno rozwiązanie): x0 = {solutions[0]}")
            else:
                print(f"Wynik (dwa rozwiązania):")
                print(f"x1 = {solutions[0]}")
                print(f"x2 = {solutions[1]}")

            print("-" * 30)

        except (SympifyError, ValueError):
            print("BŁĄD: Wprowadzono nieprawidłowe dane. Używaj liczb lub prostych wyrażeń matematycznych.")
        except Exception as e:
            print(f"BŁĄD KRYTYCZNY: Wystąpił niespodziewany problem: {e}")
        
        choice: str = input("\nCzy chcesz rozwiązać kolejne równanie? (t/n): ")
        if choice.lower() != 't':
            break

if __name__ == "__main__":
    solve_quadratic_equation()