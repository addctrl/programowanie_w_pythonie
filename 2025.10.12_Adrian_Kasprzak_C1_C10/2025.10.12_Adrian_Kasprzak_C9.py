"""
ZADANIE C9:
Napisz program, który sprawdza, czy 10-cyfrowa wartość wprowadzona przez
użytkownika reprezentuje poprawny identyfikator ISBN-10.
Zasada: Suma cyfr pomnożonych przez wagi od 10 do 1 musi dzielić się przez 11.
"""

def validate_isbn10(isbn):
    # Czyszczenie numeru ISBN z myślników i spacji
    clean_isbn = isbn.replace("-", "").replace(" ", "")
    
    # ISBN-10 musi mieć dokładnie 10 znaków
    if len(clean_isbn) != 10:
        return False
    
    # Sprawdzamy czy to same cyfry
    if not clean_isbn.isdigit():
        return False
        
    total_sum = 0
    weight = 10
    
    # Iterujemy po każdej cyfrze
    for char in clean_isbn:
        digit = int(char)
        total_sum += digit * weight
        weight -= 1 # Waga maleje: 10, 9, 8...
        
    # Warunek poprawności: suma podzielna przez 11
    return total_sum % 11 == 0

def main():
    print("--- Zadanie C9: Walidator ISBN-10 ---")
    
    user_input = input("Podaj numer ISBN-10: ")
    
    if validate_isbn10(user_input):
        print("To jest POPRAWNY numer ISBN-10.")
    else:
        print("To NIE jest poprawny numer.")

    input("\nNaciśnij Enter, aby zakończyć.")

if __name__ == "__main__":
    main()