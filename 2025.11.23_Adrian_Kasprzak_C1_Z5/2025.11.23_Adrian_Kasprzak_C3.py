"""
Ćwiczenie 3:
Program oblicza całki nieoznaczone i oznaczone.
Użytkownik wprowadza funkcję, zmienną oraz (opcjonalnie) granice całkowania.
Obsługuje nieskończoność (oznaczenie 'oo').
"""

from sympy import symbols, integrate, sympify, SympifyError, oo, pprint, init_printing
from sympy.core.symbol import Symbol

def calculate_integral() -> None:
    # Inicjalizacja ładnego drukowania (ASCII art dla wzorów)
    init_printing(use_unicode=True)

    print("--- KALKULATOR CAŁEK (Sympy) ---")
    print("Wpisz 'q' w dowolnym momencie, aby wyjść.")
    print("Dla nieskończoności użyj symbolu: oo (dwa małe 'o').")

    while True:
        try:
            print("\n" + "-"*30)
            
            # 1. Pobranie funkcji
            func_str = input("Podaj wzór funkcji (np. x**2 + sin(x)): ")
            if func_str.lower() in ['q', 'quit', 'exit']:
                break
            
            expression = sympify(func_str)

            # 2. Pobranie zmiennej (domyślnie x)
            var_str = input("Podaj zmienną całkowania [domyślnie x]: ").strip()
            if not var_str:
                var_str = 'x'
            
            variable = Symbol(var_str)

            # 3. Wybór trybu
            mode = input("Całka [O]znaczona czy [N]ieoznaczona? (o/n): ").strip().lower()

            if mode == 'n':
                # Całka nieoznaczona
                print("Obliczam całkę nieoznaczoną...")
                result = integrate(expression, variable)
                print("\nWYNIK:")
                pprint(result)
                print("(+ stała C)")

            elif mode == 'o':
                # Całka oznaczona
                limit_from = input(f"Granica dolna (od): ")
                limit_to = input(f"Granica górna (do): ")

                # Konwersja granic (obsługa 'oo' i '-oo')
                a = sympify(limit_from)
                b = sympify(limit_to)

                print(f"Obliczam całkę oznaczoną od {a} do {b}...")
                result = integrate(expression, (variable, a, b))
                
                print("\nWYNIK:")
                pprint(result)
                
                # Próba wyświetlenia wartości zmiennoprzecinkowej, jeśli wynik jest liczbą
                try:
                    val = float(result.evalf())
                    print(f"Wartość przybliżona: {val:.4f}")
                except:
                    pass
            else:
                print("BŁĄD: Nieznany tryb. Wybierz 'o' lub 'n'.")

        except SympifyError:
            print("BŁĄD SKŁADNI: Nieprawidłowe wyrażenie. Pamiętaj o mnożeniu (2*x) i potęgowaniu (x**2).")
        except Exception as e:
            print(f"BŁĄD KRYTYCZNY: {e}")

if __name__ == "__main__":
    calculate_integral()