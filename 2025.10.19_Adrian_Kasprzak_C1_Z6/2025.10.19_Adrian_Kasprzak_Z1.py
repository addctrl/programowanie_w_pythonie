"""
ZADANIE Z1: Analiza obrazu (dane_z1.txt)
Obraz: 320 kolumn x 200 wierszy.
Piksele: 0-255.

1. Najjaśniejszy (max) i najciemniejszy (min) piksel.
2. Ile wierszy usunąć, by obraz miał pionową oś symetrii.
3. Liczba pikseli kontrastujących (różnica > 128 z dowolnym sąsiadem).
"""

def main():
    print("--- Zadanie Z1: Analiza obrazu ---")
    
    # 1. WCZYTANIE DANYCH DO MACIERZY (Lista list)
    obraz = []
    try:
        with open("dane_z1.txt", "r") as f:
            for linia in f:
                # strip() usuwa entery, split() dzieli po spacjach
                # int() zamienia napis na liczbę
                wiersz = [int(x) for x in linia.strip().split()]
                if wiersz: # zabezpieczenie przed pustą linią
                    obraz.append(wiersz)
    except FileNotFoundError:
        print("Błąd: Brak pliku dane_z1.txt!")
        return

    # Wymiary obrazu
    ilosc_wierszy = len(obraz)      # Powinno być 200
    ilosc_kolumn = len(obraz[0])    # Powinno być 320

    print(f"Wczytano obraz: {ilosc_kolumn}x{ilosc_wierszy}")

    # --- PODPUNKT 1: MAX i MIN ---
    # Spłaszczamy listę, żeby łatwo znaleźć min/max, albo iterujemy.
    # Użyjemy zagnieżdżonej pętli dla jasności.
    
    max_jasnosc = -1
    min_jasnosc = 256
    
    for r in range(ilosc_wierszy):
        for c in range(ilosc_kolumn):
            piksel = obraz[r][c]
            if piksel > max_jasnosc:
                max_jasnosc = piksel
            if piksel < min_jasnosc:
                min_jasnosc = piksel

    # --- PODPUNKT 2: SYMETRIA ---
    # Obraz ma pionową oś symetrii, jeśli wiersz jest palindromem.
    # Musimy policzyć wiersze, które NIE SĄ symetryczne (do usunięcia).
    
    wiersze_do_usuniecia = 0
    
    for wiersz in obraz:
        # Pythonowy trik na odwrócenie listy: wiersz[::-1]
        # Jeśli wiersz różni się od swojego odbicia, to nie jest symetryczny
        wiersz_odwrocony = wiersz[::-1]
        if wiersz != wiersz_odwrocony:
            wiersze_do_usuniecia += 1

    # --- PODPUNKT 3: KONTRAST ---
    # Piksel jest kontrastujący, jeśli ma CHOCIAŻ JEDNEGO sąsiada
    # z różnicą > 128. Sąsiedzi: lewo, prawo, góra, dół.
    
    liczba_kontrastujacych = 0
    
    for r in range(ilosc_wierszy):
        for c in range(ilosc_kolumn):
            jest_kontrast = False
            aktualny = obraz[r][c]
            
            # Sprawdzamy sąsiada z DOŁU (jeśli nie jesteśmy w ostatnim wierszu)
            if r < ilosc_wierszy - 1:
                if abs(aktualny - obraz[r+1][c]) > 128:
                    jest_kontrast = True
            
            # Sprawdzamy sąsiada z GÓRY (jeśli nie jesteśmy w pierwszym wierszu)
            if r > 0:
                if abs(aktualny - obraz[r-1][c]) > 128:
                    jest_kontrast = True
                    
            # Sprawdzamy sąsiada z PRAWEJ (jeśli nie jesteśmy w ostatniej kolumnie)
            if c < ilosc_kolumn - 1:
                if abs(aktualny - obraz[r][c+1]) > 128:
                    jest_kontrast = True
            
            # Sprawdzamy sąsiada z LEWEJ (jeśli nie jesteśmy w pierwszej kolumnie)
            if c > 0:
                if abs(aktualny - obraz[r][c-1]) > 128:
                    jest_kontrast = True
            
            if jest_kontrast:
                liczba_kontrastujacych += 1

    # --- ZAPIS WYNIKÓW ---
    with open("dane_z1_wyniki.txt", "w") as f_out:
        f_out.write(f"1. Najjasniejszy: {max_jasnosc}, Najciemniejszy: {min_jasnosc}\n")
        f_out.write(f"2. Wiersze do usuniecia: {wiersze_do_usuniecia}\n")
        f_out.write(f"3. Piksele kontrastujace: {liczba_kontrastujacych}\n")

    print("-" * 30)
    print("WYNIKI:")
    print(f"Max: {max_jasnosc}, Min: {min_jasnosc}")
    print(f"Do usunięcia: {wiersze_do_usuniecia}")
    print(f"Kontrastujące: {liczba_kontrastujacych}")
    print("\nZapisano w dane_z1_wyniki.txt")
    
    input("\nEnter, aby zakończyć.")

if __name__ == "__main__":
    main()