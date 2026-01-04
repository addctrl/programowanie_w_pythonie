
"""
Ćwiczenie C1: 
Ciąg tekstowy T składa się z losowych cyfr i liter alfabetu angielskiego.
Znajdź przynajmniej jeden najdłuższy podciąg ciągu T, który składa się z
samych cyfr, przy czym te cyfry tworzą podciąg niemalejący.
"""

import sys

def find_longest_non_decreasing_digits(text: str) -> str:
    """
    Znajduje najdłuższy podciąg cyfr w tekście, który jest niemalejący.
    
    Args:
        text (str): Ciąg wejściowy.
        
    Returns:
        str: Najdłuższy podciąg spełniający warunki. Jeśli brak, zwraca pusty ciąg.
    """
    if not text:
        return ""

    max_substring = ""
    current_substring = ""

    for char in text:
        if char.isdigit():
            # Jeśli to pierwsza cyfra w nowej sekwencji LUB cyfra jest większa/równa poprzedniej
            if not current_substring or char >= current_substring[-1]:
                current_substring += char
            else:
                # Koniec sekwencji niemalejącej
                if len(current_substring) > len(max_substring):
                    max_substring = current_substring
                current_substring = char # Start nowej sekwencji od bieżącej cyfry
        else:
            # Znak nie jest cyfrą - resetujemy sekwencję
            if len(current_substring) > len(max_substring):
                max_substring = current_substring
            current_substring = ""

    # Sprawdzenie po zakończeniu pętli, jeśli ciąg kończy się cyframi
    if len(current_substring) > len(max_substring):
        max_substring = current_substring

    return max_substring

def main():
    print("--- ZADANIE C1: Najdłuższy podciąg niemalejący cyfr ---")
    
    # Dane testowe z treści zadania
    test_case = "dfgnqeiut98tna1223v0w3r123334asdsh"
    expected = "123334"
    
    print(f"Ciąg testowy: {test_case}")
    result = find_longest_non_decreasing_digits(test_case)
    print(f"Wynik: {result}")
    
    if result == expected:
        print("STATUS: TEST OK")
    else:
        print(f"STATUS: BŁĄD (Oczekiwano: {expected})")

    # Tryb interaktywny dla użytkownika
    print("\n--- Tryb użytkownika ---")
    try:
        user_input = input("Podaj własny ciąg znaków (lub wciśnij Enter by zakończyć): ").strip()
        if user_input:
            user_result = find_longest_non_decreasing_digits(user_input)
            print(f"Najdłuższy podciąg dla Twoich danych: '{user_result}'")
        else:
            print("Pusto. Kończymy.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    main()