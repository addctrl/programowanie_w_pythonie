"""
ZADANIE C3:
1. Utwórz plik dane_c3.txt z podaną listą słów.
2. Wczytaj słowa i przepisz do wyniki_c3.txt tylko te, 
   które mają parzystą liczbę znaków.
"""

def main():
    lista_slow = [
        "absolutny", "adapter", "adnotacja", "adres", "bariera", 
        "basen", "bat", "bateria", "baza", "beczka", 
        "bestia", "bez", "cel", "celny", "cena"
    ]

    print("--- Zadanie C3: Filtracja słów (parzysta długość) ---")

    # Generowanie pliku z danymi
    with open("dane_c3.txt", "w", encoding="utf-8") as f_out:
        for slowo in lista_slow:
            f_out.write(slowo + "\n")

    # Odczyt i filtracja
    # Sprawdzamy modulo 2 z długości słowa (len % 2 == 0)
    with open("dane_c3.txt", "r", encoding="utf-8") as f_in, \
         open("wyniki_c3.txt", "w", encoding="utf-8") as f_res:
        
        for line in f_in:
            word = line.strip()
            if len(word) % 2 == 0:
                f_res.write(word + "\n")
                print(f"Znaleziono: {word} ({len(word)} znaków)")

    print("-" * 30)
    print("Zapisano wyniki do pliku wyniki_c3.txt")
    input("\nEnter, aby zakończyć.")

if __name__ == "__main__":
    main()