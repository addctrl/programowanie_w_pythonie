"""
Ćwiczenie C4:
Oblicz wartość sqrt(13) oraz PI wykorzystując podane ułamki łańcuchowe.
O dokładności obliczeń decyduje użytkownik.
"""

import sys

def calculate_sqrt13(precision_scale: int):
    """
    Oblicza sqrt(13) iteracyjnie.
    Wzór: val = 4 / (6 + val)
    Wynik końcowy: 3 + val
    
    Args:
        precision_scale (int): Wykładnik dokładności (np. 6 -> epsilon 1e-6)
    """
    epsilon = 10 ** (-precision_scale - 1) # Margines błędu mniejszy niż wyświetlana precyzja
    current_val = 0.0
    previous_val = -1.0
    iterations = 0
    
    # Pętla działa dopóki zmiana wyniku jest większa niż epsilon
    while abs(current_val - previous_val) > epsilon:
        previous_val = current_val
        # Rekurencja: 4 / (6 + poprzednia_wartość)
        current_val = 4.0 / (6.0 + current_val)
        iterations += 1
        
        # Bezpiecznik na wypadek pętli nieskończonej
        if iterations > 10000:
            break
            
    # Dodajemy część całkowitą, której brakuje w czystym ułamku
    result = 3.0 + current_val
    return result, iterations

def calculate_pi(iterations: int):
    """
    Oblicza PI wg wzoru Brounckera.    
    Wzór: 4/PI = 1 + 1^2 / (2 + 3^2 / (2 + 5^2 / ...))
    """
    # Zaczynamy od dołu - najgłębszy poziom ułamka
    # Przyjmujemy startową wartość 0 na samym dnie
    current_val = 0.0
    
    # Iterujemy od N w dół do 1
    for k in range(iterations, 0, -1):
        numerator = (2 * k - 1) ** 2
        denominator = 2.0
        
        # Krok ułamka
        current_val = numerator / (denominator + current_val)
        
    # Finalne przekształcenie wg wzoru: 4/PI = 1 + wynik
    pi_approx = 4.0 / (1.0 + current_val)
    return pi_approx

def main():
    print("Ćwiczenie C4: Ułamki Łańcuchowe")
    
    try:
        user_input = input("Podaj liczbę miejsc po przecinku (np. 5): ").strip()
        if not user_input.isdigit():
            print("Błąd: Podaj liczbę całkowitą.")
            return
            
        places = int(user_input)
        if places < 1 or places > 15:
            print("Info: Dla standardowego float w Pythonie sensowna precyzja to max 15 cyfr.")
        
        # Obliczenie SQRT(13)
        sqrt_val, sqrt_iters = calculate_sqrt13(places)
        
        # Obliczenie PI
        # Wzór Brounckera zbiega wolno. Żeby uzyskać N miejsc po przecinku, 
        # trzeba wykonać sporo iteracji. Dajemy mnożnik dla bezpieczeństwa.
        pi_iters = places * 2500 + 1000 # Empiryczny mnożnik dla Brounckera
        pi_val = calculate_pi(pi_iters)

        print("-" * 40)
        print(f"WYNIKI (Precyzja wyświetlania: {places})")
        print("-" * 40)
        
        # Formatowanie wyniku dynamicznie do liczby miejsc
        fmt = f"{{:.{places}f}}"
        
        print(f"SQRT(13): {fmt.format(sqrt_val)}")
        print(f"   -> Osiągnięto w {sqrt_iters} iteracjach idąc od góry pierwiastka.")
        print(f"   -> Check (math.sqrt): {13**0.5}")
        
        print(f"\nPI      : {fmt.format(pi_val)}")
        print(f"   -> Użyto {pi_iters} iteracji idać od dołu pierwiastka.")
        print(f"   -> Check (math.pi)  : 3.141592653589793")
        
        print("-" * 40)

    except ValueError:
        print("Błąd: Nieprawidłowe dane wejściowe.")
    except Exception as e:
        print(f"Błąd systemu: {e}")

if __name__ == "__main__":
    main()