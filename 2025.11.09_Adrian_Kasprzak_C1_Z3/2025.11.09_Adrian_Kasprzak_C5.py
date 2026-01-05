def atbash_cipher(text):
    """
    Szyfruje lub deszyfruje tekst metodą At Bash.
    Algorytm jest symetryczny - ta sama funkcja służy do obu operacji.
    """
    result = []
    
    # Konwersja na wielkie litery - spełnienie wymogu
    clean_text = text.upper()
    
    for char in clean_text:
        # Sprawdzamy czy znak jest literą z zakresu A-Z (ASCII 65-90)
        if 'A' <= char <= 'Z':
            # Logika: Odwrócenie indeksu w alfabecie
            # Kod ASCII: A=65, Z=90.
            # Wzór: Nowy = 'Z' - (Stary - 'A')
            original_index = ord(char) - ord('A')
            reversed_code = ord('Z') - original_index
            result.append(chr(reversed_code))
        else:
            # Znaki niebędące literami (spacje, cyfry) przepisujemy bez zmian
            # Dzięki temu zachowujemy strukturę zdania.
            result.append(char)
            
    return "".join(result)

def main():
    print("--- Zadanie C5: szyfr at bash ---")
    print("Symetryczny szyfr podstawieniowy: A<->Z, B<->Y itd.")
    
    # Test automatyczny na podstawie przykładu z PDF 
    test_input = "UNIWERSYTET POMORSKI"
    expected_output = "FMRDVIHBGVG KLNLIHPR"
    test_result = atbash_cipher(test_input)
    
    if test_result == expected_output:
        print(f"Test: OK (Testowy ciąg przetworzony poprawnie).")
    else:
        print(f"Test: BŁĄD! Oczekiwano {expected_output}, otrzymano {test_result}")

    while True:
        try:
            print("\nCo chcesz zrobić?")
            print("1. Szyfrowanie / deszyfrowanie")
            print("2. Wyjście")
            
            choice = input("Wybór: ").strip()
            
            if choice == '2':
                break
                
            if choice == '1':
                user_text = input("Podaj tekst (wielkie litery, bez polskich znaków): ")
                
                # Walidacja - ostrzeżenie jeśli user wpisał polskie znaki lub małe litery
                # Program automatycznie je naprawi (upper), ale warto dać info.
                if not user_text.isascii():
                    print("Uwaga: Wykryto znaki spoza ASCII (np. polskie ogonki). Mogą nie zostać przetworzone.")
                
                processed_text = atbash_cipher(user_text)
                
                print("-" * 30)
                print(f"WEJŚCIE: {user_text.upper()}")
                print(f"WYJŚCIE: {processed_text}")
                print("-" * 30)
            
            else:
                print("Nieznana opcja.")
                
        except Exception as e:
            print(f"Wystąpił nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    main()