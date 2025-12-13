"""
ZADANIE C5:
Napisz program zawierający funkcję, który sprawdza, czy dana liczba naturalna 
jest "podzielna", tj. jest większa od zera i dzieli się całkowicie przez 
sumę swoich cyfr (taką liczbą jest np. 21). 
Ponadto - zgodnie z wyborem użytkownika - program powinien generować 
wszystkie liczby podzielne do 10000.
"""


def digit_sum(n):
    """
    Funkcja pomocnicza obliczająca sumę cyfr liczby.
    Sposób 'Pythonic': zamiana na napis, iteracja po znakach, konwersja na int.
    """
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

def is_divisible(n):
    """
    Sprawdza warunki zadania:
    1. n > 0
    2. n % digit_sum(n) == 0
    """
    if n <= 0:
        return False
    
    sum = digit_sum(n)
    
    # Zabezpieczenie, choć dla n>0 suma cyfr zawsze >0
    if sum == 0: 
        return False
        
    return n % sum == 0

def main():
    print("=== Liczby Nivena ===")
    print("Wybierz tryb pracy:")
    print("1 - Sprawdź konkretną liczbę")
    print("2 - Wygeneruj wszystkie liczby podzielne do 10000")
    
    choice = input("Twój wybór (1 lub 2): ")

    if choice == '1':
        try:
            number = int(input("Podaj liczbę całkowitą: "))
            if is_divisible(number):
                sum = digit_sum(number)
                print(f"TAK. Liczba {number} dzieli się przez sumę cyfr ({sum}).")
            else:
                sum = digit_sum(number)
                print(f"NIE. Liczba {number} nie dzieli się przez sumę cyfr ({sum}).")
        except ValueError:
            print("Błąd: To nie jest poprawna liczba.")

    elif choice == '2':
        print("\nGeneruję liczby podzielne z zakresu 1 - 10000:")
        found = []
        
        # Iterujemy od 1 do 10000 włącznie
        for i in range(1, 10001):
            if is_divisible(i):
                found.append(i)
        
        # Wypisanie wyników w czytelnej formie
        print(f"Znaleziono {len(found)} takich liczb.")
        print("Oto one:")
        print(found) 
        
    else:
        print("Nieznana opcja. Uruchom program ponownie.")

    input("\nAby zakończyć program, naciśnij klawisz Enter.")

if __name__ == "__main__":
    main()
