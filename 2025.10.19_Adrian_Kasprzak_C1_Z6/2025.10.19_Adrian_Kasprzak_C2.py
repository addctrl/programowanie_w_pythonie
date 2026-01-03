"""
ZADANIE C2:
W pliku dane_c2.txt znajduje się w oddzielnych wierszach 100 par oddzielonych spacją liczb z przedziału [5, 500].
Napisz program, który odczytuje dane z pliku wejściowego, a następnie przepisuje do pliku wyniki_c2.txt tylko te
iloczyny par liczb zapisanych w kolejnych wierszach, które mieszczą się w przedziale [250, 10000].
"""

def main():
    print("--- Zadanie C2: Filtrowanie iloczynów ---")

    # Otwieramy plik z danymi (odczyt) i plik wynikowy (zapis)
    # Stosujemy blok with, żeby pliki same się zamknęły po wykonaniu
    with open("dane_c2.txt", "r") as plik_dane, \
         open("wyniki_c2.txt", "w") as plik_wyniki:
        
        # Iterujemy przez każdą linię w pliku wejściowym
        for linia in plik_dane:
            # Usuwamy białe znaki (np. enter na końcu linii)
            linia = linia.strip()
            
            # Zabezpieczenie: jeśli linia jest pusta, idziemy dalej
            if not linia:
                continue
            
            # Dzielimy linię po spacji (split tworzy listę napisów)
            liczby = linia.split()
            
            # Zamieniamy napisy na liczby całkowite (int)
            # Zakładamy, że w linii są zawsze dwie liczby
            a = int(liczby[0])
            b = int(liczby[1])
            
            iloczyn = a * b
            
            # Sprawdzamy czy mieści się w przedziale [250, 10000]
            if iloczyn >= 250 and iloczyn <= 10000:
                # Jeśli pasuje, zapisujemy do pliku
                # Musimy zamienić liczbę na napis (str) i dodać nową linię (\n)
                plik_wyniki.write(str(iloczyn) + "\n")
                
                # Wypisujemy też na ekran dla podglądu (opcjonalnie)
                print(f"Pasuje: {a} * {b} = {iloczyn}")

    print("-" * 30)
    print("Zadanie wykonane. Sprawdź plik wyniki_c2.txt")
    
    input("\nNaciśnij Enter, aby zakończyć.")

if __name__ == "__main__":
    main()