import random
import os

FILENAME_NAMES = "imiona.txt"
FILENAME_SURNAMES = "nazwiska.txt"

def setup_files():
    """
    Tworzy pliki z danymi, jeśli nie istnieją, abyś nie musiał klepać tego ręcznie.
    Automatyzacja nudy = wyższa efektywność.
    """
    if not os.path.exists(FILENAME_NAMES):
        print(f"Generuję plik {FILENAME_NAMES}...")
        with open(FILENAME_NAMES, 'w', encoding='utf-8') as f:
            # Format: Imie;plec (m/k)
            data = [
                "Anna;k", "Maria;k", "Katarzyna;k", "Małgorzata;k", "Agnieszka;k",
                "Barbara;k", "Ewa;k", "Krystyna;k", "Elżbieta;k", "Zofia;k",
                "Piotr;m", "Krzysztof;m", "Andrzej;m", "Tomasz;m", "Jan;m",
                "Paweł;m", "Michał;m", "Marcin;m", "Jakub;m", "Adam;m"
            ]
            f.write("\n".join(data))

    if not os.path.exists(FILENAME_SURNAMES):
        print(f"Generuję plik {FILENAME_SURNAMES}...")
        with open(FILENAME_SURNAMES, 'w', encoding='utf-8') as f:
            # Format: NazwiskoMeskie;NazwiskoZenskie
            data = [
                "Nowak;Nowak", "Kowalski;Kowalska", "Wiśniewski;Wiśniewska", "Wójcik;Wójcik",
                "Kowalczyk;Kowalczyk", "Kamiński;Kamińska", "Lewandowski;Lewandowska",
                "Zieliński;Zielińska", "Szymański;Szymańska", "Woźniak;Woźniak",
                "Dąbrowski;Dąbrowska", "Kozłowski;Kozłowska", "Jankowski;Jankowska",
                "Mazur;Mazur", "Wojciechowski;Wojciechowska", "Kwiatkowski;Kwiatkowska",
                "Krawczyk;Krawczyk", "Kaczmarek;Kaczmarek", "Piotrowski;Piotrowska", "Grabowski;Grabowska"
            ]
            f.write("\n".join(data))

def generate_profiles(count=50):
    """
    Generuje unikalne profile osobowe.
    """
    try:
        # Wczytywanie i segregacja danych
        names_m, names_f = [], []
        surnames_data = [] # Lista krotek (meskie, zenskie)

        with open(FILENAME_NAMES, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(';')
                if len(parts) == 2:
                    name, gender = parts
                    if gender.lower() == 'm':
                        names_m.append(name)
                    else:
                        names_f.append(name)

        with open(FILENAME_SURNAMES, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(';')
                if len(parts) == 2:
                    surnames_data.append((parts[0], parts[1]))

        # Walidacja danych wejściowych
        if not names_m or not names_f or not surnames_data:
            print("Błąd: Puste lub uszkodzone pliki danych.")
            return

        # Generowanie unikalnych kombinacji
        generated_profiles = set()
        attempts = 0
        max_attempts = count * 10  # Zabezpieczenie przed pętlą nieskończoną

        print(f"\nGenerowanie {count} unikalnych profili...")

        while len(generated_profiles) < count and attempts < max_attempts:
            attempts += 1
            
            # Losuj płeć (0 - M, 1 - K)
            is_female = random.choice([True, False])
            
            if is_female:
                imie = random.choice(names_f)
                # Wybierz nazwisko z pary (index 1 dla kobiet)
                nazwisko_entry = random.choice(surnames_data)
                nazwisko = nazwisko_entry[1]
            else:
                imie = random.choice(names_m)
                # Wybierz nazwisko z pary (index 0 dla mężczyzn)
                nazwisko_entry = random.choice(surnames_data)
                nazwisko = nazwisko_entry[0]

            full_name = f"{imie} {nazwisko}"
            
            if full_name not in generated_profiles:
                generated_profiles.add(full_name)

        #  Wynik
        print("-" * 30)
        for i, profile in enumerate(generated_profiles, 1):
            print(f"{i}. {profile}")
        print("-" * 30)
        
        if len(generated_profiles) < count:
            print(f"Uwaga: Wygenerowano tylko {len(generated_profiles)} unikalnych kombinacji (możliwe, że pula danych jest za mała).")

    except FileNotFoundError:
        print("Błąd: Nie znaleziono plików. Uruchom program ponownie.")
    except Exception as e:
        print(f"Krytyczny błąd: {e}")

if __name__ == "__main__":
    setup_files() 
    generate_profiles(50)