"""
ZADANIE C4:
Znajdź w liście v wszystkie podciągi trójelementowe (trzy kolejne cyfry),
które tworzą ciągi niemalejące.
"""

def main():
    # Dane wejściowe z treści zadania 
    v = [1, 2, 4, 3, 6, 8, 7, 7, 8, 3, 4, 5, 6, 7, 1, 3, 9, 1, 0, 4, 2, 3, 6, 9]

    print("--- Zadanie C4: Podciągi niemalejące ---")
    
    # Iterujemy do len(v) - 2, bo pobieramy elementy i+1 oraz i+2.
    # Gdybyśmy szli do końca, wyrzuci IndexError.
    for i in range(len(v) - 2):
        
        # Pobranie trójki sąsiednich liczb
        a, b, c = v[i], v[i+1], v[i+2]
        
        # Warunek ciągu niemalejącego: a <= b <= c
        if a <= b and b <= c:
            print(f"Znaleziono podciąg (indeks {i}): {a}, {b}, {c}")

    print("-" * 30)
    input("Enter, aby zakończyć.")

if __name__ == "__main__":
    main()