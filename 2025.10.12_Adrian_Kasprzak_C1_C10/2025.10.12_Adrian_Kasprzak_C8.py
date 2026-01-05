def is_semiprime(n):
    # Liczby mniejsze od 4 nie mogą być półpierwsze, bo najmniejsza to 2*2=4
    if n < 4:
        return False

    factors_count = 0
    d = 2
    temp = n

    # Szukamy dzielników do pierwiastka z liczby
    while d * d <= temp:
        while temp % d == 0:
            factors_count += 1
            temp //= d
        d += 1

    # Jeśli po pętli coś zostało (np. 17 w liczbie 34), to jest to ostatni czynnik
    if temp > 1:
        factors_count += 1

    return factors_count == 2

def main():
    print("--- Zadanie C8: Liczby Półpierwsze ---")
    
    try:
        user_input = int(input("Podaj liczbę całkowitą: "))
        
        if is_semiprime(user_input):
            print(f"TAK. Liczba {user_input} JEST półpierwsza.")
        else:
            print(f"NIE. Liczba {user_input} NIE JEST półpierwsza.")
            
    except ValueError:
        print("Błąd: To nie jest poprawna liczba.")

    input("\nAby zakończyć program, naciśnij klawisz Enter.")

if __name__ == "__main__":
    main()