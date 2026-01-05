import math

# Stały tekst z zadania
DEFAULT_TEXT = "JESTEM STUDENTEM INFORMATYKI UNIWERSYTETU POMORSKIEGO"
ALPHABET_SIZE = 26

def prepare_text(text: str) -> str:
    """
    Usuwa spacje i znaki niebędące literami, konwertuje na UPPERCASE.
    """
    return "".join(c.upper() for c in text if c.isalpha())

def get_modular_inverse(a: int, m: int) -> int:
    """
    Znajduje odwrotność modularną liczby 'a' modulo 'm'.
    Czyli szuka takiego x, że (a * x) % m == 1.
    """
    try:
        return pow(a, -1, m)
    except ValueError:
        return None

def affine_cipher(text: str, a: int, b: int, decrypt: bool = False) -> str:
    """
    Logika szyfru afinicznego.
    """
    # Walidacja klucza 'a' 
    if math.gcd(a, ALPHABET_SIZE) != 1:
        raise ValueError(f"Klucz 'a' ({a}) nie jest względnie pierwszy z {ALPHABET_SIZE}. Deszyfrowanie niemożliwe.")

    result = []
    
    # Dla deszyfrowania potrzebujemy odwrotności a
    if decrypt:
        a_inv = get_modular_inverse(a, ALPHABET_SIZE)
        if a_inv is None:
             raise ValueError("Nie znaleziono odwrotności modularnej (błąd matematyczny).")

    for char in text:
        x = ord(char) - ord('A')
        
        if decrypt:
            # D(x) = a**(-1) * (x - b) mod m
            val = (a_inv * (x - b)) % ALPHABET_SIZE
        else:
            # E(x) = (ax + b) mod m
            val = (a * x + b) % ALPHABET_SIZE
            
        result.append(chr(val + ord('A')))
        
    return "".join(result)

def main():
    print("--- ZADANIE Z2: Szyfr Afiniczny ---")
    
    while True:
        print("\n" + "="*30)
        print("MENU:")
        print("1. Szyfrowanie / Deszyfrowanie")
        print("Q. Wyjście")
        choice = input("Twój wybór: ").strip().upper()
        
        if choice == 'Q':
            break
        if choice != '1':
            continue

        try:
            # Pytamy o tekst
            print(f"\nPodaj tekst (ENTER dla domyślnego: '{DEFAULT_TEXT[:20]}...'):")
            user_input = input("> ").strip()
            
            if not user_input:
                final_input = prepare_text(DEFAULT_TEXT)
                print("Info: Używam tekstu domyślnego.")
            else:
                final_input = prepare_text(user_input)
                
            if not final_input:
                print(">>> BŁĄD: Tekst nie zawiera liter.")
                continue

            # Pytamy o klucze a i b
            print("\nPodaj klucze (wzór: ax + b).")
            print("Uwaga: 'a' musi być liczbą nieparzystą różną od 13 (np. 3, 5, 7, 9, 11...).")
            
            a_str = input("Podaj a: ").strip()
            b_str = input("Podaj b: ").strip()
            
            if not a_str.lstrip('-').isdigit() or not b_str.lstrip('-').isdigit():
                print(">>> BŁĄD: Klucze muszą być liczbami całkowitymi.")
                continue
                
            a = int(a_str)
            b = int(b_str)

            # Walidacja wstępna klucza
            if math.gcd(a, ALPHABET_SIZE) != 1:
                print(f"BŁĄD KRYTYCZNY: 'a'={a} i 26 mają wspólny dzielnik. Szyfr nieodwracalny. Wybierz inne 'a'.")
                continue

            # Operacja
            print("\nCo robimy?")
            print("A. Szyfruj")
            print("B. Deszyfruj")
            op = input("Wybór (A/B): ").strip().upper()
            
            if op not in ['A', 'B']:
                print("Błędny wybór.")
                continue
                
            decrypt_mode = (op == 'B')
            
            # Wykonanie
            out = affine_cipher(final_input, a, b, decrypt=decrypt_mode)
            
            print("-" * 40)
            print(f"OPERACJA: {'Deszyfrowanie' if decrypt_mode else 'Szyfrowanie'}")
            print(f"KLUCZE: a={a}, b={b}")
            print(f"INPUT: {final_input}")
            print(f"OUTPUT:{out}")
            print("-" * 40)

        except ValueError as ve:
            print(f"BŁĄD LOGICZNY: {ve}")
        except Exception as e:
            print(f"BŁĄD SYSTEMU: {e}")

if __name__ == "__main__":
    main()