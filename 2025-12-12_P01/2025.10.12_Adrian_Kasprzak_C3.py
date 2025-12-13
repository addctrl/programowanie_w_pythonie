"""
ZADANIE C3 (Rozszerzone):
Napisz program, który rozwiązuje równanie kwadratowe. 
Dodatkowo: obsługuje liczby rzeczywiste oraz zespolone dla delty ujemnej.
Współczynniki (a, b, c) podaje użytkownik.
"""

import cmath 

def main():
    print("=== Rozwiązywanie równania kwadratowego ===")
    
    try:
        a = float(input("Podaj współczynnik a: "))
        b = float(input("Podaj współczynnik b: "))
        c = float(input("Podaj współczynnik c: "))
    except ValueError:
        print("Błąd: Współczynniki muszą być liczbami.")
        return

    if a == 0:
        print("To nie jest równanie kwadratowe (a nie może wynosić 0).")
        return

    # Obliczanie delty
    delta = b**2 - 4*a*c
    print(f"\nDelta wynosi: {delta}")

    # Pierwiastkowanie (cmath.sqrt -> obsługuje ujemne delta)
    sqrt_delta = cmath.sqrt(delta)

    x1 = (-b - sqrt_delta) / (2 * a)
    x2 = (-b + sqrt_delta) / (2 * a)

    if delta > 0:
        # Delta dodatnia - dwa rozwiązania rzeczywiste
        # .real, aby wyświetlić czystą liczbę bez jej części zespolonej
        print(f"Równanie ma dwa pierwiastki rzeczywiste:")
        print(f"x1 = {x1.real:.2f}")
        print(f"x2 = {x2.real:.2f}")
    elif delta == 0:
        # Delta zerowa - jeden pierwiastek
        print(f"Równanie ma jeden pierwiastek rzeczywisty: x0 = {x1.real:.2f}")
    else:
        # Delta ujemna - wyniki zespolone
        print("Równanie nie ma pierwiastków w zbiorze liczb rzeczywistych.")
        print(f"Rozwiązania zespolone:")
        print(f"x1 = {x1:.2f}") 
        print(f"x2 = {x2:.2f}")

    input("\nAby zakończyć program, naciśnij klawisz Enter.")

if __name__ == "__main__":
    main()