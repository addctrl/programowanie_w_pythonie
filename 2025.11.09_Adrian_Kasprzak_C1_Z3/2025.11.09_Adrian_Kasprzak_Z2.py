import sys

FILENAME = "wypadki.txt"

WOJEWODZTWA_MAP = {
    'D': 'Dolnośląskie', 'C': 'Kujawsko-pomorskie', 'L': 'Lubelskie',
    'F': 'Lubuskie', 'E': 'Łódzkie', 'K': 'Małopolskie',
    'W': 'Mazowieckie', 'O': 'Opolskie', 'R': 'Podkarpackie',
    'B': 'Podlaskie', 'G': 'Pomorskie', 'S': 'Śląskie',
    'T': 'Świętokrzyskie', 'N': 'Warmińsko-mazurskie', 'P': 'Wielkopolskie',
    'Z': 'Zachodniopomorskie'
}

def analyze_data():
    stats = {code: {'name': name, 'total': 0, 'powiaty': {}} 
             for code, name in WOJEWODZTWA_MAP.items()}

    print(f"--- Rozpoczynam analizę pliku: {FILENAME} ---")
    
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            for line_no, line in enumerate(file, 1):
                line = line.strip()
                if not line: continue
                
                parts = line.split()
                # Oczekujemy formatu: KOD DATA LICZBA (np. GS 2023-07-01 3)
                if len(parts) < 3:
                    continue 

                powiat_code = parts[0]
                try:
                    count = int(parts[2])
                except ValueError:
                    print(f"Błąd danych w linii {line_no}: '{parts[2]}' nie jest liczbą.")
                    continue

                # Rozpoznawanie województwa po pierwszej literze
                woj_key = powiat_code[0]
                
                if woj_key in stats:
                    stats[woj_key]['total'] += count
                    current = stats[woj_key]['powiaty'].get(powiat_code, 0)
                    stats[woj_key]['powiaty'][powiat_code] = current + count

        # GENEROWANIE RAPORTU
        
        # 1. Województwo z największą liczbą wypadków
        max_accidents = -1
        top_voivodeships = []
        
        for key, data in stats.items():
            if data['total'] > max_accidents:
                max_accidents = data['total']
                top_voivodeships = [data['name']]
            elif data['total'] == max_accidents and max_accidents > 0:
                top_voivodeships.append(data['name']) # Obsługa remisów 

        print("\n=== WYNIKI ANALIZY ===")
        print(f"1. Najbardziej niebezpieczne województwa (Suma: {max_accidents}):")
        print(f"   -> {', '.join(top_voivodeships)}")

        # 2. Najniebezpieczniejszy powiat w każdym województwie
        print("\n2. Najniebezpieczniejsze powiaty wg województw:")
        for data in stats.values():
            if data['total'] == 0: continue
            
            powiaty = data['powiaty']
            if not powiaty: continue
            
            local_max = max(powiaty.values())
            # Znajdź wszystkie powiaty z tym maksimum (remisy)
            worst_powiats = [p for p, c in powiaty.items() if c == local_max]
            
            print(f"   [{data['name']}] -> {', '.join(worst_powiats)} ({local_max} wypadków)")

        # 3. Statystyka dla Pomorskiego (GS + GSL)
        print("\n3. Statystyka regionu słupskiego (Woj. Pomorskie):")
        pomorskie = stats.get('G')
        if pomorskie and pomorskie['total'] > 0:
            sum_slupsk = pomorskie['powiaty'].get('GS', 0) + pomorskie['powiaty'].get('GSL', 0)
            percent = (sum_slupsk / pomorskie['total']) * 100
            print(f"   Suma wypadków w woj. pomorskim: {pomorskie['total']}")
            print(f"   Słupsk (GS) + Powiat (GSL): {sum_slupsk}")
            print(f"   Udział procentowy: {percent:.2f}%")
        else:
            print("   Brak danych dla województwa pomorskiego.")

    except FileNotFoundError:
        print(f"BŁĄD: Nie widzę pliku '{FILENAME}' w katalogu roboczym.")

if __name__ == "__main__":
    analyze_data()