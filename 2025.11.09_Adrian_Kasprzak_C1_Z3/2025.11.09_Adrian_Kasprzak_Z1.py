# Słownik mapujący znaki na kod Morse'a (standard międzynarodowy)
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.'
}

# Odwrócony słownik do dekodowania (Morse -> znak)
REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    """Zamienia tekst na ciąg Morse'a."""
    clean_text = text.upper().strip()
    morse_output = []
    
    for char in clean_text:
        if char in MORSE_CODE_DICT:
            morse_output.append(MORSE_CODE_DICT[char])
        else:
            print(f"Pominięto nieobsługiwany znak: {char}")
            
    # Znaki w Morsie oddzielamy jedną spacją dla czytelności
    return " ".join(morse_output)

def morse_to_text(morse_code):
    """Zamienia kod Morse'a na tekst."""
    text_output = []
    # Dzielimy ciąg wejściowy po spacjach
    tokens = morse_code.split(' ')
    
    for token in tokens:
        if token in REVERSE_MORSE_DICT:
            text_output.append(REVERSE_MORSE_DICT[token])
        elif token == '':
            continue
        else:
            text_output.append('?') # Znak błędu dla nieznanego kodu
            
    return "".join(text_output)

def main():
    print("--- Zadanie Z1: translator Morse'a ---")
    
    while True:
        print("\nWybierz tryb:")
        print("1. Tekst -> Morse")
        print("2. Morse -> Tekst (Opcjonalne)")
        print("3. Wyjście")
        
        choice = input("Twój wybór: ").strip()
        
        if choice == '1':
            user_input = input("Podaj tekst (A-Z, 0-9, bez polskich znaków): ")
            # Zgodnie z poleceniem  usuwamy spacje z inputu, 
            user_input_cleaned = user_input.replace(" ", "")
            
            result = text_to_morse(user_input_cleaned)
            print(f"WYNIK: {result}")
            
        elif choice == '2':
            print("Instrukcja: Wpisz kropki (.) i kreski (-), oddzielając litery spacją.")
            user_input = input("Podaj kod Morse'a: ")
            result = morse_to_text(user_input)
            print(f"WYNIK: {result}")
            
        elif choice == '3':
            break
        else:
            print("Nieznana opcja.")

if __name__ == "__main__":
    main()