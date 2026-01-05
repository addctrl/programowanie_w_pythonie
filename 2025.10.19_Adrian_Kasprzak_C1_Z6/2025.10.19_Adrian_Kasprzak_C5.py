def main():
    # Dane wejściowe
    v1 = [1, 3, 5, 7, 9]
    v2 = [1, 4, 7, 11, 15]
    v3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

    print("--- Zadanie C5: Operacje na zbiorach (bez użycia set) ---")

    # A) Część wspólna v1 i v2 (Intersection)
    # Elementy, które są w v1 ORAZ w v2
    wspolne_v1_v2 = []
    for x in v1:
        if x in v2:
            wspolne_v1_v2.append(x)
            
    print(f"a) Część wspólna v1 i v2: {wspolne_v1_v2}")

    # B) Różnica v3 - (v1 U v2)
    # Krok 1: Obliczamy sumę v1 i v2 (bez duplikatów)
    suma_v1_v2 = []
    
    # Dodajemy wszystko z v1
    for x in v1:
        suma_v1_v2.append(x)
        
    # Dodajemy z v2 tylko to, czego jeszcze nie ma (unikalność)
    for x in v2:
        if x not in suma_v1_v2:
            suma_v1_v2.append(x)

    # Krok 2: Odejmujemy tę sumę od v3
    # Element jest w v3, ale NIE MA go w sumie v1+v2
    roznica = []
    for x in v3:
        if x not in suma_v1_v2:
            roznica.append(x)

    print(f"b) Różnica v3 - (v1 U v2): {roznica}")

    # C) Suma wszystkich zbiorów v1 U v2 U v3
    # Bazujemy na obliczonej wcześniej sumie_v1_v2 i dodajemy v3
    suma_total = list(suma_v1_v2) # Kopia listy, żeby nie psuć poprzedniej zmiennej
    
    for x in v3:
        if x not in suma_total:
            suma_total.append(x)

    # Sortujemy dla czytelności wyniku
    suma_total.sort()
    print(f"c) Suma v1 U v2 U v3: {suma_total}")

    input("\nEnter, aby zakończyć.")

if __name__ == "__main__":
    main()