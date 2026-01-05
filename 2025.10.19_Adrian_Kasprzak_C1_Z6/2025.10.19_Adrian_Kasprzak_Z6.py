def main():
    print("--- Zadanie Z6: Analiza trasy (Podjazdy vs Zjazdy) ---")
    
    try:
        with open("dane_z6.txt", "r", encoding='utf-8') as plik:
            for linia in plik:
                linia = linia.strip()
                if not linia:
                    continue

                # Krok 1: Parsowanie linii
                # Format: "Nr: wys1 wys2 wys3..."
                czesci = linia.split(":")
                nr_etapu = czesci[0]
                
                # Zamiana ciągu wysokości na listę liczb całkowitych
                # np. "434 365 291..." -> [434, 365, 291...]
                wysokosci_str = czesci[1].split()
                punkty_wysokosci = [int(x) for x in wysokosci_str]

                # Liczniki dla danego etapu
                liczba_podjazdow = 0
                liczba_zjazdow = 0

                # Krok 2: Analiza odcinków
                # Iterujemy po parach sąsiednich punktów (i oraz i+1)
                # Jeśli punktów jest N, to odcinków jest N-1
                ilosc_punktow = len(punkty_wysokosci)
                
                for i in range(ilosc_punktow - 1):
                    poczatek_odcinka = punkty_wysokosci[i]
                    koniec_odcinka = punkty_wysokosci[i+1]
                    
                    # Definicja PODJAZDU: początek < koniec (wspinamy się)
                    if poczatek_odcinka < koniec_odcinka:
                        liczba_podjazdow += 1
                        
                    # Definicja ZJAZDU: początek > koniec (zjeżdżamy)
                    elif poczatek_odcinka > koniec_odcinka:
                        liczba_zjazdow += 1
                        
                    # Jeśli są równe (odcinek płaski), nie robimy nic (zgodnie z "Uwagą")

                # Krok 3: Weryfikacja warunku zadania
                # "wypisujący numery tych etapów, w których podjazdów było mniej niż zjazdów"
                if liczba_podjazdow < liczba_zjazdow:
                    print(f"Etap {nr_etapu}: Podjazdów {liczba_podjazdow}, Zjazdów {liczba_zjazdow}")

    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku dane_z6.txt w katalogu roboczym.")
    except ValueError:
        print("Błąd danych: Plik zawiera wpisy, które nie są liczbami.")

    input("\nNaciśnij Enter, aby zakończyć.")

if __name__ == "__main__":
    main()