import random

CONF_SIZE = 25
CONF_RANGE = (-100, 100)

def generate_random_list(size, val_range):
    return [random.randint(val_range[0], val_range[1]) for _ in range(size)]

def find_max(data):
    if not data:
        raise ValueError("Pusta lista")
    return max(data)

def main():
    print("--- Zadanie C6: Największa liczba w tablicy ---")
    
    try:
        # Generowanie tablicy
        dataset = generate_random_list(CONF_SIZE, CONF_RANGE)
        print(f"Wygenerowana tablica: {dataset}")

        # Szukanie najwiekszej wartosci
        max_val = find_max(dataset)
        print(f"Największa wartość: {max_val}")
        
    except ValueError as e:
        print(f"Błąd: {e}")

    input("\nAby zakończyć program, naciśnij klawisz Enter.")

if __name__ == "__main__":
    main()