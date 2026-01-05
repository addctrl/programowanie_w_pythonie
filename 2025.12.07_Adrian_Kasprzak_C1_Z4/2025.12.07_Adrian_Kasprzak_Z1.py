# Stały tekst z zadania
DEFAULT_TEXT = "JESTEM STUDENTEM INFORMATYKI UNIWERSYTETU POMORSKIEGO"

def prepare_text(text: str) -> str:
    """
    Usuwa spacje i znaki niebędące literami, konwertuje na UPPERCASE.
    """
    return "".join(c.upper() for c in text if c.isalpha())

def vigenere_cipher(text: str, key: str, decrypt: bool = False) -> str:
    if not key:
        return text
    
    key = prepare_text(key)
    if not key:
        raise ValueError("Klucz musi zawierać litery!")
        
    result = []
    key_len = len(key)
    
    for i, char in enumerate(text):
        shift = ord(key[i % key_len]) - ord('A')
        current_val = ord(char) - ord('A')
        
        if decrypt:
            # D = (C - K) mod 26
            new_val = (current_val - shift) % 26
        else:
            # E = (P + K) mod 26
            new_val = (current_val + shift) % 26
            
        result.append(chr(new_val + ord('A')))
        
    return "".join(result)

def generate_playfair_matrix(key: str):
    key = prepare_text(key).replace('J', 'I')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # Bez J
    
    matrix_list = []
    seen = set()
    
    for char in key:
        if char not in seen:
            seen.add(char)
            matrix_list.append(char)
            
    for char in alphabet:
        if char not in seen:
            seen.add(char)
            matrix_list.append(char)
            
    coords = {}
    grid = [['' for _ in range(5)] for _ in range(5)]
    
    for idx, char in enumerate(matrix_list):
        row = idx // 5
        col = idx % 5
        coords[char] = (row, col)
        grid[row][col] = char
        
    return grid, coords

def prepare_playfair_text(text: str) -> list:
    text = text.replace('J', 'I')
    digrams = []
    i = 0
    while i < len(text):
        a = text[i]
        
        if i + 1 < len(text):
            b = text[i+1]
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            b = 'X'
            i += 1
            
        digrams.append((a, b))
    return digrams

def playfair_cipher(text: str, key: str, decrypt: bool = False) -> str:
    grid, coords = generate_playfair_matrix(key)
    
    if not decrypt:
        digrams = prepare_playfair_text(text)
    else:
        # Przy deszyfracji zakładamy, że input jest już parzysty, ale na wszelki wypadek czyścimy go
        text = text.replace('J', 'I')
        if len(text) % 2 != 0:
            text += 'X' 
        digrams = [(text[i], text[i+1]) for i in range(0, len(text), 2)]

    result = []
    shift = -1 if decrypt else 1
    
    for a, b in digrams:
        try:
            r1, c1 = coords[a]
            r2, c2 = coords[b]
            
            if r1 == r2:
                new_a = grid[r1][(c1 + shift) % 5]
                new_b = grid[r2][(c2 + shift) % 5]
            elif c1 == c2:
                new_a = grid[(r1 + shift) % 5][c1]
                new_b = grid[(r2 + shift) % 5][c2]
            else:
                new_a = grid[r1][c2]
                new_b = grid[r2][c1]
                
            result.append(new_a + new_b)
        except KeyError:
            # Jeśli w inpucie zostały jakieś śmieci mimo czyszczenia
            continue
        
    return "".join(result)

def main():
    print("ZADANIE Z1: Vigenere lub Playfair")
    
    while True:
        print("\n" + "="*30)
        print("WYBIERZ ALGORYTM:")
        print("1. Vigenere")
        print("2. Playfair")
        print("Q. Wyjście")
        algo_choice = input("Twój wybór: ").strip().upper()
        
        if algo_choice == 'Q':
            break
        if algo_choice not in ['1', '2']:
            print(">>> BŁĄD: Wybierz 1 lub 2.")
            continue
            
        # Pytamy o klucz
        key = input("Podaj KLUCZ (tylko litery): ").strip().upper()
        if not prepare_text(key):
            print(">>> BŁĄD: Klucz nie może być pusty ani składać się z samych cyfr!")
            continue

        # Pytamy o operację
        print("\nWYBIERZ OPERACJĘ:")
        print("A. Szyfrowanie (Encrypt)")
        print("B. Deszyfrowanie (Decrypt)")
        op_choice = input("Twój wybór (A/B): ").strip().upper()
        
        if op_choice not in ['A', 'B']:
            print(">>> BŁĄD: Wpisz 'A' lub 'B'. Nie '1', nie '2', tylko litery.")
            continue
            
        decrypt_mode = (op_choice == 'B')
        op_name = "Deszyfrowanie" if decrypt_mode else "Szyfrowanie"

        # Pytamy o tekst 
        print(f"\nPodaj tekst do operacji: {op_name}")
        print(f"(Wciśnij ENTER aby użyć domyślnego: '{DEFAULT_TEXT[:20]}...')")
        user_input = input("> ").strip()
        
        if not user_input:
            final_input = prepare_text(DEFAULT_TEXT)
            print(f"Info: Używam tekstu domyślnego.")
        else:
            final_input = prepare_text(user_input)
            
        if not final_input:
            print("BŁĄD: Tekst nie zawiera żadnych liter do przetworzenia.")
            continue

        # Wykonanie
        try:
            if algo_choice == '1':
                out = vigenere_cipher(final_input, key, decrypt=decrypt_mode)
                algo_name = "Vigenere"
            else:
                out = playfair_cipher(final_input, key, decrypt=decrypt_mode)
                algo_name = "Playfair"
                
            print("-" * 40)
            print(f"ALGORYTM: {algo_name}")
            print(f"KLUCZ: {prepare_text(key)}") # Pokaż klucz po czyszczeniu
            print(f"INPUT: {final_input}")
            print(f"OUTPUT: {out}")
            print("-" * 40)
            
        except Exception as e:
            print(f"BŁĄD KRYTYCZNY: {e}")

if __name__ == "__main__":
    main()