"""
Ćwiczenie 2:
Program rozwiązuje układy równań z 2, 3 lub 4 niewiadomymi.
Użytkownik wybiera liczbę niewiadomych, a system dobiera odpowiednie symbole.
Obsługuje błędy parsowania i brak rozwiązań.
"""

from sympy import symbols, solve, SympifyError, sympify
from typing import Tuple

def get_symbols_for_mode(mode: int) -> Tuple:
    """Zwraca krotkę symboli w zależności od liczby niewiadomych."""
    if mode == 2:
        return symbols('x y')
    elif mode == 3:
        return symbols('x y z')
    elif mode == 4:
        return symbols('w x y z')
    else:
        raise ValueError("Nieobsługiwana liczba niewiadomych.")

def solve_system_of_equations() -> None:
    print("--- ROZWIĄZYWANIE UKŁADÓW RÓWNAŃ ---")
    print("Dostępne tryby: 2, 3 lub 4 niewiadome.")
    print("UWAGA: Równania wpisuj w postaci przeniesionej na jedną stronę (równa się 0).")
    print("Przykład: zamiast 'x = y + 2', wpisz 'x - y - 2'.")

    while True:
        try:
            # Wybór trybu
            mode_input = input("\nIle niewiadomych? (2/3/4) [lub 'q' by wyjść]: ").strip().lower()
            if mode_input in ['q', 'quit', 'exit']:
                break
            
            if mode_input not in ['2', '3', '4']:
                print("BŁĄD: Wybierz 2, 3 lub 4.")
                continue

            num_vars = int(mode_input)
            current_symbols = get_symbols_for_mode(num_vars)
            
            # Wyświetlenie instrukcji jakie symbole są aktywne
            print(f"Używaj symboli: {', '.join([s.name for s in current_symbols])}")

            equations = []
            print(f"Podaj {num_vars} równania/eń:")

            for i in range(num_vars):
                eq_str = input(f"Równanie {i+1}: ")
                # Konwersja stringa na wyrażenie sympy
                eq_expr = sympify(eq_str)
                equations.append(eq_expr)

            # Rozwiązanie układu
            print("\nPrzetwarzanie...")
            result = solve(equations, current_symbols, dict=True)

            # Prezentacja wyników
            if not result:
                print("Wynik: Układ sprzeczny lub brak rozwiązań.")
            else:
                print("Rozwiązanie(a):")
                for idx, sol in enumerate(result, 1):
                    print(f"--- Opcja {idx} ---")
                    # Wyświetlamy posortowane wyniki dla czytelności
                    for sym in current_symbols:
                        if sym in sol:
                            print(f"{sym} = {sol[sym]}")
                        else:
                            # Czasami solve zwraca wynik zależny od parametru, jeśli układ jest nieoznaczony
                            print(f"{sym} = (zmienna wolna)")

        except SympifyError:
            print("BŁĄD: Nieprawidłowy format równania. Sprawdź składnię (np. 2*x zamiast 2x).")
        except Exception as e:
            print(f"BŁĄD KRYTYCZNY: {e}")

if __name__ == "__main__":
    solve_system_of_equations()