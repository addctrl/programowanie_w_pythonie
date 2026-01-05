def main():
    print("--- Zadanie Z3: Piramida liczbowa ---")
    
    # 1. POBIERANIE DANYCH
    # Wersja testowa (zgodna z przykładem w PDF):
    # dane_wejsciowe = [2, 5, 7, 11, 10, 3, 0]
    
    # Wersja interaktywna (wymagana w zadaniu):
    print("Podaj od 5 do 10 liczb całkowitych oddzielonych spacją.")
    try:
        tekst = input("Twoje liczby: ")
        # Zamiana napisu na listę liczb (split tnie po spacji, int zamienia na liczbę)
        dane_wejsciowe = [int(x) for x in tekst.split()]
    except ValueError:
        print("Błąd: Wprowadzono niepoprawne dane (to nie są liczby całkowite).")
        return

    # Walidacja długości (zgodnie z treścią zadania: 5-10 liczb)
    ilosc = len(dane_wejsciowe)
    if ilosc < 5 or ilosc > 10:
        print(f"Błąd: Wprowadzono {ilosc} liczb. Wymagane od 5 do 10.")
        # Możemy tu zrobić return, ale student pewnie by pozwolił programowi działać dalej
        # więc zostawiam tylko ostrzeżenie.
        
    # 2. OBLICZANIE POZIOMÓW (od dołu do góry)
    # Przechowujemy wszystkie poziomy w liście list
    wszystkie_poziomy = []
    
    # Dodajemy podstawę (kopia listy, żeby nie psuć oryginału)
    aktualny_poziom = list(dane_wejsciowe)
    wszystkie_poziomy.append(aktualny_poziom)
    
    # Pętla działa dopóki mamy więcej niż 1 liczbę w poziomie
    while len(aktualny_poziom) > 1:
        nastepny_poziom = []
        
        # Iterujemy do przedostatniego elementu
        for i in range(len(aktualny_poziom) - 1):
            # Suma dwóch sąsiadów: obecny + następny
            suma = aktualny_poziom[i] + aktualny_poziom[i+1]
            nastepny_poziom.append(suma)
            
        # Dodajemy nowy poziom do listy wyników
        wszystkie_poziomy.append(nastepny_poziom)
        # Ustawiamy nowy poziom jako aktualny do następnej iteracji
        aktualny_poziom = nastepny_poziom

    # 3. WYŚWIETLANIE PIRAMIDY (od góry do dołu)
    print("\nWynik (Piramida):")
    print("-" * 30)
    
    # Musimy wiedzieć jak szeroka jest podstawa (w znakach), żeby wycentrować resztę.
    # Zamieniamy liczby na napisy i łączymy spacjami
    napis_baza = " ".join([str(x) for x in dane_wejsciowe])
    szerokosc_bazy = len(napis_baza) + 10 # Dodajemy margines dla bezpieczeństwa
    
    # Odwracamy listę poziomów, bo obliczaliśmy od dołu, a drukujemy od góry
    # reversed() odwraca kolejność
    for poziom in reversed(wszystkie_poziomy):
        # Zamiana listy liczb na ładny napis oddzielony spacjami
        napis_poziom = " ".join([str(x) for x in poziom])
        
        # center() centruje napis w podanej szerokości
        print(napis_poziom.center(szerokosc_bazy))

    input("\nNaciśnij Enter, aby zakończyć.")

if __name__ == "__main__":
    main()