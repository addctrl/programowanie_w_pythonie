import random

def validate_number_rules(num_str: str) -> tuple[bool, str]:
    """
    Sprawdza, czy liczba spełnia wszystkie zasady.
    Zwraca (True, "OK") lub (False, "Opis błędu").
    """
    # Długość
    if len(num_str) != 10:
        return False, f"Zła długość: {len(num_str)}"

    # Nie zaczyna się od 0
    if num_str[0] == '0':
        return False, "Zaczyna się od 0"

    # Suma cyfr >= 30
    digits = [int(d) for d in num_str]
    if sum(digits) < 30:
        return False, f"Suma cyfr za mała ({sum(digits)})"

    # Trzecia cyfra nieparzysta
    if digits[2] % 2 == 0:
        return False, f"Trzecia cyfra ({digits[2]}) jest parzysta"

    # Sąsiedzi
    # "żadne bezpośrednio sąsiadujące cyfry nie mogą być identyczne, chyba że są to dwie ostatnie"
    # Sprawdzamy pary do przedostatniej (i == 8)
    for i in range(8):
        if num_str[i] == num_str[i+1]:
            return False, f"Powtórzenie na pozycji {i}-{i+1} ({num_str[i]}{num_str[i+1]})"

    return True, "OK"


def generate_compliant_number() -> str:
    """Generuje liczbę spełniającą wszystkie kryteria."""
    
    while True:
        # Budujemy liczbę cyfra po cyfrze
        digits = []

        # Cyfra 1
        # Nie może być 0
        digits.append(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))

        # Cyfra 2
        # Nie może być taka sama jak poprzednia
        candidates = [d for d in range(10) if d != digits[-1]]
        digits.append(random.choice(candidates))

        # Cyfra 3
        # Musi być NIEPARZYSTA i różna od poprzedniej
        # Nieparzyste: 1, 3, 5, 7, 9
        odd_numbers = [1, 3, 5, 7, 9]
        candidates = [d for d in odd_numbers if d != digits[-1]]
        digits.append(random.choice(candidates))

        # Cyfry 4 do 9
        # Reguła sąsiadów: różna od poprzedniej
        for _ in range(3, 9):
            prev = digits[-1]
            candidates = [d for d in range(10) if d != prev]
            digits.append(random.choice(candidates))

        # Cyfra 10
        # Ostatnia cyfra. MOŻE być taka sama jak przedostatnia.
        # Więc bierzemy dowolną z zakresu 0-9.
        digits.append(random.choice(list(range(10))))

        # Weryfikacja sumy
        if sum(digits) >= 30:
            return "".join(map(str, digits))
        
        # Jeśli suma < 30, pętla kręci się dalej 

def main():
    print("--- GENERATOR LICZB ---")
    print("Rozpoczynam test generowania 10 000 próbek")

    TARGET_COUNT = 10000
    failures = 0
    sample_numbers = []

    try:
        for i in range(TARGET_COUNT):
            # Generuj
            num = generate_compliant_number()
            
            # Waliduj 
            is_valid, reason = validate_number_rules(num)
            
            if not is_valid:
                failures += 1
                print(f"BŁĄD GENERATORA! Liczba: {num}, Powód: {reason}")
            
            # 20 próbek do wyświetlenia
            if i < 20:
                sample_numbers.append(num)

            # Prosty pasek postępu co 1000 liczb
            if (i + 1) % 1000 == 0:
                print(f"Postęp: {i + 1}/{TARGET_COUNT}...")

        print("\n" + "="*40)
        print(f"RAPORT KOŃCOWY:")
        print(f"Przetworzono liczb: {TARGET_COUNT}")
        print(f"Liczba błędów: {failures}")
        
        if failures == 0:
            print("STATUS: SUKCES")
        else:
            print("STATUS: PORAŻKA")

        print("\nPrzykładowe wygenerowane liczby:")
        for s in sample_numbers:
            print(f"-> {s} (Suma: {sum(int(d) for d in s)})")
            
    except KeyboardInterrupt:
        print("\nPrzerwano przez użytkownika.")

if __name__ == "__main__":
    main()