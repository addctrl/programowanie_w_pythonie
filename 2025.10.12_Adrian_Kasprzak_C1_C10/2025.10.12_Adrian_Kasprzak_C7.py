import random

# Konfiguracja
ARRAY_SIZE = 10
VAL_RANGE = (-50, 50)

def generate_random_list(size, val_range):
    return [random.randint(val_range[0], val_range[1]) for _ in range(size)]

def shift_right(data):
    """
    Wykonuje cykliczne przesunięcie listy w prawo.
    Wykorzystuje slicing dla czytelności i wydajności w Pythonie.
    """
    if not data:
        return data
    
    # Bierze ostatni element (jako listę) i skleja z resztą (bez ostatniego)
    return data[-1:] + data[:-1]

def main():
    print("--- Zadanie C7: Przesuniecie w prawo ---")

    # Generowanie
    original_list = generate_random_list(ARRAY_SIZE, VAL_RANGE)
    print(f"Przed zmianą: {original_list}")

    # Przesunięcie
    shifted_list = shift_right(original_list)
    print(f"Po zmianie:   {shifted_list}")

    # Weryfikacja 
    if original_list[-1] == shifted_list[0] and original_list[0] == shifted_list[1]:
        print("Status: OK (Przesunięcie poprawne)")
    else:
        print("Status: BŁĄD")

    input("\nAby zakończyć program, naciśnij klawisz Enter.")

if __name__ == "__main__":
    main()