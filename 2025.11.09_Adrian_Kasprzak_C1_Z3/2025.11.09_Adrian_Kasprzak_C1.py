"""
ZADANIE C1: 
System generowania i weryfikacji loginów
Program generuje loginy dla pracowników, weryfikuje siłę haseł oraz zarządza
prostą bazą danych użytkowników w pliku tekstowym.

DEFINICJE I ZASADY:
1. LOGIN: Składa się z pierwszych 3 liter imienia, pierwszych 3 liter nazwiska
   oraz ostatnich 3 cyfr identyfikatora.
   Przykład: Karina Zieniewicz 044396 -> KarZie396.
2. HASŁO: Musi mieć min. 8 znaków, zawierać małe i wielkie litery oraz cyfrę.
3. BAZA DANYCH: Loginy i hasła są zapisywane w pliku tekstowym (format: login;hasło).

CEL:
Umożliwić rejestrację nowych użytkowników (zapis do pliku) oraz weryfikację
istniejących (odczyt z pliku).
"""

import os

DB_FILENAME = "users_db.txt"

def get_login_name(first, last, idnumber):
    """
    Generuje login na podstawie imienia, nazwiska i ID.
    Zasada: 3 litery imienia + 3 litery nazwiska + 3 ostatnie cyfry ID.
    """
    # Zabezpieczenie przed zbyt krótkimi danymi (extra robustness)
    part1 = first[0:3] if len(first) >= 3 else first
    part2 = last[0:3] if len(last) >= 3 else last
    
    # Obsługa ID - bierzemy 3 ostatnie znaki
    if len(idnumber) >= 3:
        part3 = idnumber[-3:]
    else:
        part3 = idnumber

    return part1 + part2 + part3

def is_password_valid(password):
    """
    Weryfikuje poprawność hasła zgodnie z regułami bezpieczeństwa.
    Wymogi: długość > 7, min. 1 duża litera, min. 1 mała litera, min. 1 cyfra.
    """
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
            
    return has_upper and has_lower and has_digit

def save_credentials(login, password):
    """Zapisuje parę login i hasło do pliku."""
    try:
        with open(DB_FILENAME, "a", encoding='utf-8') as file:
            file.write(f"{login};{password}\n")
        return True
    except IOError:
        print("Błąd krytyczny: Nie można zapisać danych do pliku.")
        return False

def verify_credentials(input_login, input_password):
    """Sprawdza czy podany login i hasło istnieją w bazie."""
    if not os.path.exists(DB_FILENAME):
        return False, "Baza danych jest pusta lub nie istnieje."

    try:
        with open(DB_FILENAME, "r", encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                # Rozdzielenie loginu i hasła
                stored_login, stored_password = line.split(";")
                
                if stored_login == input_login:
                    if stored_password == input_password:
                        return True, "Zalogowano pomyślnie."
                    else:
                        return False, "Błędne hasło."
            
            return False, "Nie znaleziono użytkownika o takim loginie."
            
    except ValueError:
        return False, "Błąd struktury pliku bazy danych."
    except IOError:
        return False, "Błąd odczytu pliku."

def main():
    print("--- Zadanie C1: System generowania i weryfikacji loginów ---")
    
    while True:
        print("\nWYBIERZ AKCJĘ:")
        print("1. Rejestracja nowego pracownika")
        print("2. Logowanie (Weryfikacja)")
        print("3. Wyjście")
        
        choice = input("Twój wybór: ").strip()
        
        if choice == '1':
            print("\n--- REJESTRACJA ---")
            try:
                imie = input("Podaj imię: ").strip()
                nazwisko = input("Podaj nazwisko: ").strip()
                id_numer = input("Podaj 6-cyfrowy identyfikator: ").strip()
                
                # Generowanie loginu
                login = get_login_name(imie, nazwisko, id_numer)
                print(f"Wygenerowany login: {login}")
                
                # Pobieranie i walidacja hasła
                while True:
                    haslo = input("Ustal hasło (min 8 znaków, mała/duża litera, cyfra): ").strip()
                    if is_password_valid(haslo):
                        break
                    print("Błąd: Hasło nie spełnia wymogów bezpieczeństwa. Spróbuj ponownie.")
                
                # Zapis
                if save_credentials(login, haslo):
                    print("Sukces: Użytkownik został zarejestrowany.")
                    
            except Exception as e:
                print(f"Wystąpił nieoczekiwany błąd: {e}")

        elif choice == '2':
            print("\n--- LOGOWANIE ---")
            in_login = input("Login: ").strip()
            in_pass = input("Hasło: ").strip()
            
            status, message = verify_credentials(in_login, in_pass)
            print(f"Wynik: {message}")

        elif choice == '3':
            print("Zamykanie systemu.")
            break
        
        else:
            print("Nieznana opcja. Wybierz 1, 2 lub 3.")

    input("\nNaciśnij Enter, aby zakończyć.")

if __name__ == "__main__":
    main()