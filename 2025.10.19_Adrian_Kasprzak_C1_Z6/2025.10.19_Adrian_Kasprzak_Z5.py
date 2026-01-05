def szyfruj_plot(tekst_jawny, wysokosc):
    """
    Szyfrowanie: Układa litery w zygzak i odczytuje wierszami.
    """
    # Jeśli płot ma wysokość 1, nic się nie zmienia
    if wysokosc == 1:
        return tekst_jawny

    # Tworzymy listę pustych napisów dla każdego wiersza płotu
    # np. dla wysokosci 3: ['', '', '']
    plot = ['' for _ in range(wysokosc)]
    
    wiersz = 0
    kierunek_dol = False  # Flaga kierunku
    
    for litera in tekst_jawny:
        # Dodajemy literę do aktualnego wiersza
        plot[wiersz] += litera
        
        # Jeśli jesteśmy na górze (0) lub na dole (wysokosc-1), zmieniamy kierunek
        if wiersz == 0 or wiersz == wysokosc - 1:
            kierunek_dol = not kierunek_dol
            
        # Przesuwamy się w górę lub w dół
        if kierunek_dol:
            wiersz += 1
        else:
            wiersz -= 1
            
    # Łączymy wszystkie wiersze w jeden napis (szyfrogram)
    szyfrogram = "".join(plot)
    return szyfrogram

def deszyfruj_plot(szyfrogram, wysokosc):
    """
    Deszyfrowanie: Odtwarzamy zygzak pustymi znakami,
    wypełniamy go literami z szyfrogramu i odczytujemy po zygzaku.
    """
    if wysokosc == 1:
        return szyfrogram

    # 1. Tworzymy pustą macierz (listę list) o wymiarach płotu
    # Wypełniamy ją None, żeby wiedzieć, gdzie mają trafić litery
    macierz = [['' for _ in range(len(szyfrogram))] for _ in range(wysokosc)]
    
    # 2. Symulujemy ruch zygzaka, żeby zaznaczyć miejsca liter gwiazdką '*'
    wiersz = 0
    kierunek_dol = False
    
    for i in range(len(szyfrogram)):
        macierz[wiersz][i] = '*' # Rezerwujemy miejsce
        
        if wiersz == 0 or wiersz == wysokosc - 1:
            kierunek_dol = not kierunek_dol
            
        if kierunek_dol:
            wiersz += 1
        else:
            wiersz -= 1
            
    # 3. Wypełniamy zaznaczone miejsca ('*') literami z szyfrogramu
    # Czytamy szyfrogram znak po znaku i wstawiamy w kolejne gwiazdki wierszami
    indeks_szyfru = 0
    for r in range(wysokosc):
        for c in range(len(szyfrogram)):
            if macierz[r][c] == '*' and indeks_szyfru < len(szyfrogram):
                macierz[r][c] = szyfrogram[indeks_szyfru]
                indeks_szyfru += 1
                
    # 4. Odczytujemy wiadomość idąc ponownie po zygzaku
    wynik = []
    wiersz = 0
    kierunek_dol = False
    
    for i in range(len(szyfrogram)):
        wynik.append(macierz[wiersz][i])
        
        if wiersz == 0 or wiersz == wysokosc - 1:
            kierunek_dol = not kierunek_dol
            
        if kierunek_dol:
            wiersz += 1
        else:
            wiersz -= 1
            
    return "".join(wynik)

def main():
    print("--- Zadanie Z5: Szyfr Płotowy ---")
    
    try:
        # Pobieranie danych (usuwamy spacje dla czytelności, choć algorytm obsłuży też ze spacjami)
        tekst = input("Podaj tekst do zaszyfrowania: ")
        klucz_str = input("Podaj wysokość płotu (klucz): ")
        klucz = int(klucz_str)
        
        if klucz < 1:
            print("Błąd: Wysokość musi być większa od 0.")
            return

        # Szyfrowanie
        zaszyfrowany = szyfruj_plot(tekst, klucz)
        print(f"\nSzyfrogram: {zaszyfrowany}")
        
        # Sprawdzenie (Deszyfrowanie)
        odszyfrowany = deszyfruj_plot(zaszyfrowany, klucz)
        print(f"Odszyfrowany: {odszyfrowany}")


    except ValueError:
        print("Błąd: Klucz musi być liczbą całkowitą.")

    input("\nNaciśnij Enter, aby zakończyć.")

if __name__ == "__main__":
    main()