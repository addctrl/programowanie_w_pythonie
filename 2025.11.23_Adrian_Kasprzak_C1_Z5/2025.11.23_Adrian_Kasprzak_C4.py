"""
Ćwiczenie 4:
Program pobiera dwie funkcje liniowe/nieliniowe od użytkownika.
1. Oblicza analitycznie punkt przecięcia.
2. Rysuje wykres obu funkcji w bibliotece Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, solve, lambdify, SympifyError

def plot_and_solve_functions() -> None:
    print("--- ANALIZATOR I WIZUALIZATOR FUNKCJI ---")
    print("Wpisz dwie funkcje zmiennej 'x' (np. 2*x + 3 oraz -x + 5).")

    x = symbols('x')

    while True:
        try:
            print("\n" + "-"*40)
            # Pobranie danych
            f1_str = input("Funkcja 1 (f1): ")
            if f1_str.lower() in ['q', 'quit', 'exit']: break
            
            f2_str = input("Funkcja 2 (f2): ")
            
            # Parsowanie
            expr1 = sympify(f1_str)
            expr2 = sympify(f2_str)

            # Rozwiązanie analityczne (f1 = f2 => f1 - f2 = 0)
            print(f"\n[ANALITYKA] Szukam punktów przecięcia dla: {expr1} = {expr2}")
            solutions = solve(expr1 - expr2, x)

            if not solutions:
                print("Wynik: Funkcje się nie przecinają (brak rozwiązań rzeczywistych).")
            else:
                print("Punkty przecięcia (x):")
                for sol in solutions:
                    # Obliczamy y dla danego x
                    y_val = expr1.subs(x, sol)
                    print(f"-> x = {sol}, y = {y_val}")

            # Wizualizacja
            print("\nGeneruję wykres...")
            
            # Konwersja wyrażeń symbolicznych na szybkie funkcje Pythonowe
            f1_lambda = lambdify(x, expr1, modules=['numpy'])
            f2_lambda = lambdify(x, expr2, modules=['numpy'])

            # Zakres osi X
            x_vals = np.linspace(-10, 10, 400)

            try:
                # Obliczanie wartości Y
                y1_vals = f1_lambda(x_vals)
                y2_vals = f2_lambda(x_vals)

                # Fix dla funkcji stałych
                if not isinstance(y1_vals, np.ndarray):
                    y1_vals = np.full_like(x_vals, y1_vals)
                if not isinstance(y2_vals, np.ndarray):
                    y2_vals = np.full_like(x_vals, y2_vals)

                # Rysowanie
                plt.figure(figsize=(10, 6))
                plt.plot(x_vals, y1_vals, label=f'f1: {expr1}', linewidth=2)
                plt.plot(x_vals, y2_vals, label=f'f2: {expr2}', linewidth=2)
                
                # Zaznaczenie punktów przecięcia na wykresie
                for sol in solutions:
                    # Rysujemy tylko jeśli rozwiązanie jest liczbą rzeczywistą i mieści się na wykresie
                    if sol.is_real:
                        sol_float = float(sol)
                        if -10 <= sol_float <= 10:
                            y_sol = float(expr1.subs(x, sol))
                            plt.plot(sol_float, y_sol, 'ro', markersize=8) # Czerwona kropka
                            plt.annotate(f'({sol_float:.2f}, {y_sol:.2f})', 
                                         (sol_float, y_sol), textcoords="offset points", xytext=(0,10), ha='center')

                plt.title("Porównanie funkcji")
                plt.xlabel("x")
                plt.ylabel("y")
                plt.axhline(0, color='black', linewidth=0.5) # Oś X
                plt.axvline(0, color='black', linewidth=0.5) # Oś Y
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.legend()
                plt.show()
                print("Wykres wyświetlony.")

            except Exception as e:
                print(f"BŁĄD RYSOWANIA: Nie udało się wygenerować wykresu dla tych funkcji. ({e})")
                print("Możliwa przyczyna: Funkcja nieciągła lub zespolona w zadanym zakresie.")

        except SympifyError:
            print("BŁĄD SKŁADNI: Sprawdź format zapisu (np. 2*x zamiast 2x).")
        except Exception as e:
            print(f"BŁĄD KRYTYCZNY: {e}")

if __name__ == "__main__":
    plot_and_solve_functions()