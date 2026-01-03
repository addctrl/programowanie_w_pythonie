"""
ZADANIE C2: 
Problem lidera i cięcia taśmy
Program znajduje liczbę sposobów przecięcia ciągu liczb na dwie części tak,
aby na obu częściach występował ten sam lider (element dominujący).

ALGORYTM:
1. Liderem zbioru jest element występujący częściej niż k/2 razy.
2. Warunek konieczny: aby liczba była liderem w obu podciągach, musi być
   liderem całego ciągu.
3. Obliczamy wystąpienia wszystkich liczb. Wyznaczamy lidera globalnego.
4. Przechodzimy przez taśmę raz, zliczając wystąpienia lidera po lewej stronie
   i sprawdzamy warunek dla obu stron dynamicznie.

INPUT:
Liczba elementów n (2 <= n <= 10000)
Ciąg liczb całkowitych.
"""

from collections import Counter

def solve_leader_cuts():
    print("--- Zadanie C2: Lider ciągu ---")
    print("Wpisz dane zgodnie z formatem (lub 'exit' aby wyjść).")
    
    while True:
        try:
            print("\nPodaj liczbę elementów (n):")
            line1 = input("> ").strip()
            if line1.lower() == 'exit':
                break
            
            if not line1: 
                continue
                
            n = int(line1)
            if not (2 <= n <= 10000):
                print("Błąd: n musi być z przedziału [2, 10000].")
                continue

            print(f"Podaj {n} liczb całkowitych oddzielonych spacją:")
            line2 = input("> ").strip()
            numbers = list(map(int, line2.split()))

            if len(numbers) != n:
                print(f"Błąd: Podałeś {len(numbers)} liczb, a zadeklarowałeś {n}.")
                continue

            # LOGIKA BIZNESOWA
            
            # 1. Znalezienie globalnego lidera
            counts = Counter(numbers)
            candidate_val, total_occurrences = counts.most_common(1)[0]
            
            # Sprawdź czy kandydat jest faktycznie liderem całości (> n/2)
            if total_occurrences <= n / 2:
                print("\nWynik: 0 cięć.")
                print("Powód: Ten ciąg nie posiada globalnego lidera, więc nie można go podzielić.")
                continue
                
            global_leader = candidate_val
            
            # 2. Szukanie poprawnych cięć
            valid_cuts_count = 0
            valid_cuts_details = [] # Do przechowywania informacji o podziale
            
            left_leader_count = 0
            total_leader_count = total_occurrences
            
            # Iterujemy od 0 do n-2 (bo cięcie musi zostawić przynajmniej 1 element z prawej)
            # i dzieli po elemencie o indeksie 'i'
            for i in range(n - 1):
                current_num = numbers[i]
                
                # Aktualizujemy licznik lidera po lewej stronie
                if current_num == global_leader:
                    left_leader_count += 1
                
                # Rozmiary części
                len_left = i + 1
                len_right = n - len_left
                
                # Liczba liderów po prawej stronie
                right_leader_count = total_leader_count - left_leader_count
                
                # WARUNEK ZADANIA:
                # Lider musi występować > połowa długości w obu częściach
                is_left_ok = left_leader_count > (len_left / 2)
                is_right_ok = right_leader_count > (len_right / 2)
                
                if is_left_ok and is_right_ok:
                    valid_cuts_count += 1
                    # Zapisz szczegóły podziału (wymagane przez zadanie)
                    # Uwaga: przy dużych danych to może być dużo tekstu, ale zadanie wymaga.
                    left_part = numbers[:i+1]
                    right_part = numbers[i+1:]
                    valid_cuts_details.append((left_part, right_part))

            # RAPORTOWANIE
            print(f"\nLiczba możliwych cięć: {valid_cuts_count}")
            
            if valid_cuts_count > 0:
                print("Szczegóły podziałów (Lewa strona | Prawa strona):")
                for idx, (l_part, r_part) in enumerate(valid_cuts_details, 1):
                    # Konwersja do stringa dla czytelności, ograniczamy długie listy w wyświetlaniu
                    l_str = str(l_part) if len(l_part) < 10 else f"[{len(l_part)} elem...]"
                    r_str = str(r_part) if len(r_part) < 10 else f"[{len(r_part)} elem...]"
                    print(f"{idx}. {l_str} | {r_str}")
            
        except ValueError:
            print("Błąd: Wprowadzono niepoprawne dane (oczekiwano liczb całkowitych).")
        except Exception as e:
            print(f"Błąd krytyczny: {e}")

if __name__ == "__main__":
    solve_leader_cuts()