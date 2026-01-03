"""
ZADANIE C4: 
Kod Graya 
Program konwertuje liczby zapisane binarnie na kod Graya i odwrotnie,
wykorzystując operacje logiczne XOR.

INPUT:
Ciąg znaków '0' i '1' (domyślnie 4-bitowy, ale kod obsłuży dowolną długość).
"""

def xor_char(a, b):
    """Pomocnicza funkcja XOR dla znaków '0' i '1'."""
    return '1' if a != b else '0'

def binary_to_gray(binary_str):
    """
    Konwertuje ciąg binarny na kod Graya.
    Wzór: g[i] = b[i] XOR b[i-1] (gdzie b[i-1] to bit bardziej znaczący)
    """
    if not binary_str:
        return ""

    # Przepisanie najstarszego bitu 
    # g[0] = b[0]
    gray_code = [binary_str[0]]

    # Iteracja dla pozostałych bitów 
    for i in range(1, len(binary_str)):
        prev_bit = binary_str[i-1]
        curr_bit = binary_str[i]
        
        # Zastosowanie XOR
        new_bit = xor_char(curr_bit, prev_bit)
        gray_code.append(new_bit)

    return "".join(gray_code)

def gray_to_binary(gray_str):
    """
    Konwertuje kod Graya na ciąg binarny.
    Wzór: b[i] = g[i] XOR b[i-1]
    """
    if not gray_str:
        return ""

    # Przepisanie najstarszego bitu
    # b[0] = g[0] 
    binary_code = [gray_str[0]]

    # Iteracja. Uzywa wcześniej wyliczonego bitu
    for i in range(1, len(gray_str)):
        curr_gray_bit = gray_str[i]
        prev_binary_bit = binary_code[i-1] # b[i-1]
        
        # b[i] = g[i] XOR b[i-1] 
        new_bin_bit = xor_char(curr_gray_bit, prev_binary_bit)
        binary_code.append(new_bin_bit)

    return "".join(binary_code)

def validate_input(input_str):
    """Sprawdza czy ciąg składa się tylko z 0 i 1."""
    for char in input_str:
        if char not in ('0', '1'):
            return False
    return True

def main():
    print("--- Zadanie C4: Kod Graya ---")
    print("Zasada: Dwie kolejne liczby w kodzie Graya różnią się tylko 1 bitem.")
    
    while True:
        print("\nWYBIERZ TRYB:")
        print("1. Binarny -> kod Graya")
        print("2. Kod Graya -> binarny")
        print("3. Wyjście")
        
        choice = input("Wybór: ").strip()
        
        if choice == '3':
            break
            
        if choice not in ('1', '2'):
            print("Błąd: Wybierz 1, 2 lub 3.")
            continue

        input_data = input("Podaj 4-bitowy ciąg (np. 1010): ").strip()
        
        # Walidacja danych wejściowych
        if not validate_input(input_data):
            print("Błąd: Ciąg musi zawierać tylko znaki 0 i 1.")
            continue
            
        if len(input_data) == 0:
            print("Błąd: Pusty ciąg.")
            continue

        # Ostrzeżenie, jeśli user poda inną długość niż 4 (ale pozwalamy na to)
        if len(input_data) != 4:
            print(f"Info: Podałeś ciąg {len(input_data)}- on nie jest czterobitowym, ale obliczę to.")

        # Przetwarzanie
        try:
            if choice == '1':
                result = binary_to_gray(input_data)
                print(f"Wynik (kod Graya):   {result}")
            else:
                result = gray_to_binary(input_data)
                print(f"Wynik (binarny): {result}")
                
        except Exception as e:
            print(f"Błąd przetwarzania: {e}")

if __name__ == "__main__":
    main()