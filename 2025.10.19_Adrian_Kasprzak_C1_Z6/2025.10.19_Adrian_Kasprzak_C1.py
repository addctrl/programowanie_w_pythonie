"""
ZADANIE C1:
Napisz program, który wykonuje kolejno następujące operacje:
a) tworzy plik o nazwie dane_c1.txt i przepisuje do niego w kolejnych wierszach nazwy kolejnych miesięcy roku. Nazwy
miesięcy są zdefiniowane w programie w postaci listy,
b) wypisuje na ekranie tylko te miesiące zawarte w pliku dane_c1.txt, których nazwa zaczyna się na literę "m".
c) wypisuje do nowego pliku o nazwie wyniki_c1.txt nazwy wszystkich miesięcy znajdujących się w pliku dane_c1.txt,
których nazwa liczy więcej niż 7 znaków.
"""

def main():
    # Lista z nazwami miesięcy (małe litery, bo tak zazwyczaj są w kalendarzu)
    miesiace = [
        "styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec",
        "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"
    ]

    print("--- Zadanie C1: Operacje na plikach (miesiące) ---")

    # --- PODPUNKT A ---
    # Tworzymy plik dane_c1.txt i zapisujemy tam miesiące
    # 'w' oznacza write (zapisywanie), encoding utf-8 żeby były polskie znaki
    with open("dane_c1.txt", "w", encoding="utf-8") as plik_dane:
        for m in miesiace:
            plik_dane.write(m + "\n")
    
    print("Plik dane_c1.txt został utworzony.")
    print("-" * 30)

    # --- PODPUNKT B i C ---
    print("Miesiące na literę 'm' (odczytane z pliku):")
    
    # Otwieramy plik z danymi do odczytu ('r')
    # I od razu otwieramy plik do zapisu wyników ('w')
    with open("dane_c1.txt", "r", encoding="utf-8") as plik_odczyt, \
         open("wyniki_c1.txt", "w", encoding="utf-8") as plik_wyniki:
        
        # czytamy plik linijka po linijce
        for linia in plik_odczyt:
            # strip() usuwa białe znaki (np. ten enter co daliśmy wcześniej)
            nazwa = linia.strip()
            
            # Podpunkt b: sprawdzamy czy zaczyna się na "m"
            if nazwa.startswith("m"):
                print(nazwa)
            
            # Podpunkt c: sprawdzamy czy jest dłuższy niż 7 znaków
            if len(nazwa) > 7:
                plik_wyniki.write(nazwa + "\n")

    print("-" * 30)
    print("Miesiące dłuższe niż 7 znaków zostały zapisane do wyniki_c1.txt")
    
    input("\nNaciśnij Enter, aby zakończyć.")

if __name__ == "__main__":
    main()