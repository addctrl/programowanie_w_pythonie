import os
from typing import List

def evaluate_rpn(expression: str) -> float:
    """
    Oblicza wartość wyrażenia ONP.
    Zwraca wynik jako float lub podnosi wyjątek w przypadku błędu.
    """
    stack: List[float] = []
    tokens = expression.split()

    if not tokens:
        raise ValueError("Pusta linia")

    for token in tokens:
        if token in ['+', '-', '*', '/']:
            if len(stack) < 2:
                raise ValueError(f"Za mało liczb na stosie dla operatora '{token}'")

            b = stack.pop() # Druga liczba w działaniu
            a = stack.pop() # Pierwsza liczba w działaniu

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Dzielenie przez zero")
                result = a / b
            
            stack.append(result)
        else:
            # Próba konwersji na liczbę
            try:
                number = float(token)
                stack.append(number)
            except ValueError:
                raise ValueError(f"Nieznany symbol: '{token}'")

    # Na końcu na stosie powinien zostać tylko wynik
    if len(stack) != 1:
        raise ValueError(f"Niejednoznaczny wynik. Pozostało na stosie: {stack}")

    return stack[0]

def process_file(filename: str):
    print(f"--- ANALIZA PLIKU: {filename} ---")
    
    if not os.path.exists(filename):
        print(f"BŁĄD KRYTYCZNY: Nie znaleziono pliku '{filename}'.")
        print("Upewnij się, że plik jest w tym samym folderze co skrypt.")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    success_count = 0
    error_count = 0

    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue

        print(f"Linia {i}: {line:<40}", end=" -> ")
        
        try:
            result = evaluate_rpn(line)
            # Formatowanie: jeśli liczba jest całkowita, wytnij ".0"
            if result.is_integer():
                print(f"WYNIK: {int(result)}")
            else:
                print(f"WYNIK: {result:.4f}")
            success_count += 1
        except ZeroDivisionError:
            print("BŁĄD: Dzielenie przez zero!")
            error_count += 1
        except Exception as e:
            print(f"BŁĄD: {e}")
            error_count += 1

    print("-" * 60)
    print(f"RAPORT: Przetworzono {success_count + error_count} linii.")
    print(f"Sukcesy: {success_count}, Błędy: {error_count}")

if __name__ == "__main__":

    FILENAME = "wyrazenia_onp.txt"
    process_file(FILENAME)