"""
ZADANIE C1:
Napisz program, który na podstawie podanej przez użytkownika liczby sekund 
wypisuje na ekranie, ile to jest dni, godzin, minut i sekund.

Zasady przesyłania: 
- Nazwa pliku: RRRR.MM.DD_Imie_Nazwisko_C1.py
- Brak polskich znaków w nazwach plików.
"""

def main():
    print("===KONWERTER SEKUND===")

    # Pobieranie danych od użytkownika
    try:
        total_seconds = int(input("Podaj liczbę sekund: "))
    except ValueError:
        print("Wprowadzono nieprawidłową wartość.")
        return
    
    # STAŁE
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTE
    SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR

    # Obliczanie
    days = total_seconds // SECONDS_IN_DAY
    remaining_seconds = total_seconds % SECONDS_IN_DAY
    
    hours = remaining_seconds // SECONDS_IN_HOUR
    remaining_seconds %= SECONDS_IN_HOUR
    
    minutes = remaining_seconds // SECONDS_IN_MINUTE
    seconds = remaining_seconds % SECONDS_IN_MINUTE

    print(f"\nWynik dla {total_seconds} sekund:")
    print(f"Dni: {days}")
    print(f"Godziny: {hours}")
    print(f"Minuty: {minutes}")
    print(f"Sekundy: {seconds}")

    input("\nAby zakończyć program, naciśnij klawisz Enter.") 

if __name__ == "__main__":
    main()