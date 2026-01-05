from datetime import date, timedelta
import calendar

WEEKDAYS_PL = {
    0: "Poniedziałek",
    1: "Wtorek",
    2: "Środa",
    3: "Czwartek",
    4: "Piątek",
    5: "Sobota",
    6: "Niedziela"
}

def is_leap(year: int) -> bool:
    """Sprawdza czy rok jest przestępny."""
    return calendar.isleap(year)

def get_date_info(year: int, day_of_year: int) -> str:
    """
    Konwertuje numer dnia w roku na sformatowany ciąg znaków.
    """
    # Walidacja zakresu roku z zadania
    if not (1900 <= year <= 2099):
        raise ValueError("Rok musi być z przedziału 1900 - 2099.")

    # Walidacja liczby dni
    days_in_year = 366 if is_leap(year) else 365
    if not (1 <= day_of_year <= days_in_year):
        raise ValueError(f"Dla roku {year} podaj dzień z zakresu 1-{days_in_year}.")

    # 1 Stycznia + (N-1) dni
    base_date = date(year, 1, 1)
    target_date = base_date + timedelta(days=day_of_year - 1)
    
    # Dzień tygodnia
    weekday_name = WEEKDAYS_PL[target_date.weekday()]
    
    # YYYY-MM-DD dzień tygodnia
    return f"{target_date} ({weekday_name})"

def main():
    print("--- Zadanie 3: Kalendarz ---")
    print("Zakres lat: 1900 - 2099")
    
    while True:
        print("\n" + "-"*30)
        user_input = input("Podaj ROK i NUMER DNIA (np. '2026 3') lub 'q' aby wyjść: ").strip()
        
        if user_input.lower() == 'q':
            break
            
        try:
            parts = user_input.split()
            if len(parts) != 2:
                print(">>> BŁĄD: Podaj dwie liczby oddzielone spacją.")
                continue
                
            year = int(parts[0])
            day_num = int(parts[1])
            
            result = get_date_info(year, day_num)
            print(f"Wynik: {result}")
            
        except ValueError as ve:
            print(f">>> BŁĄD DANYCH: {ve}")
        except Exception as e:
            print(f">>> BŁĄD SYSTEMU: {e}")

if __name__ == "__main__":
    main()