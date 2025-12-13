"""
ZADANIE C2:
Napisz program, który sprawdza, czy podany przez użytkownika rok jest przestępny. 
Rok przestępny musi się dzielić bez reszty przez 4, zaś pełne stulecia przez 400 
oraz ma swój początek w roku 1582, bo wtedy po raz pierwszy go wprowadzono.
"""

def main():
    print("=== Sprawdzanie roku przestępnego ===")
    
    try:
        year = int(input("Podaj rok: "))
    except ValueError:
        print("Blad: Podaj rok jako liczbę całkowitą.")
        return

    # Walidacja daty wprowadzenia kalendarza
    if year < 1582:
        print("Kalendarz gregorianski (i lata przestępne w tym modelu) obowiązuje od 1582 roku.")
    else:
        # Logika: Rok jest przestępny gdy:
        # (podzielny przez 4 && niepodzielny przez 100) || (podzielny przez 400)
        # Przykładowe lata przestępne: 2020, 2024, 2028
        # Przykładowe lata nieprzestępne: 1900, 2100, 1991
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"Rok {year} JEST przestępny.")
        else:
            print(f"Rok {year} NIE JEST przestępny.")

    input("\nAby zakończyć program, naciśnij klawisz Enter.")

if __name__ == "__main__":
    main()