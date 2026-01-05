import os

class StudentData:
    """Struktura przechowująca dane jednej osoby dla czytelności kodu."""
    def __init__(self, id_osoby, scores):
        self.id = id_osoby
        self.scores = scores 
        self.min_score = min(scores)
        self.max_score = max(scores)
        self.avg_score = sum(scores) / len(scores)
        self.diff = self.max_score - self.min_score

def parse_file(filename):
    data = []
    
    if not os.path.exists(filename):
        print(f"BŁĄD: Brak pliku '{filename}'.")
        return []

    print(f"Wczytuję dane z: {filename}...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Pomijamy header
            header = next(f) 
            
            for line_num, line in enumerate(f, 2):
                line = line.strip()
                if not line: continue
                
                parts = line.split('\t')
                
                # Walidacja struktury wiersza, muszą być 4 kolumny
                if len(parts) < 4:
                    print(f"Ostrzeżenie: Nieprawidłowa linia {line_num}: {line}")
                    continue
                
                try:
                    # Konwersja floatów, przecinek na kropke
                    scores = [float(x.replace(',', '.')) for x in parts[:3]]
                    
                    # Konwersja id na int
                    id_osoby = int(parts[3])
                    
                    # Tworzymy obiekt i dodajemy do listy
                    data.append(StudentData(id_osoby, scores))
                    
                except ValueError as e:
                    print(f"Błąd parsowania w linii {line_num}: {e}")

    except Exception as e:
        print(f"BŁĄD KRYTYCZNY ODCZYTU PLIKU: {e}")
        return []

    print(f"Pomyślnie załadowano {len(data)} rekordów.")
    return data

def analyze_data(data):
    if not data:
        print("Brak danych do analizy.")
        return

    print("\n--- WYNIKI ANALIZY ---")

    # 1. Ile osób w przynajmniej jednym teście uzyskało wynik poniżej 10,00%?
    count_below_10 = sum(1 for p in data if p.min_score < 10.0)
    print(f"1. Liczba osób z wynikiem < 10%: {count_below_10}")

    # 2. Ile osób osiągnęło takie wyniki testów, że różnica pomiędzy dwoma 
    # dowolnymi z nich nigdy nie przekracza 2,00%?
    count_stable = sum(1 for p in data if p.diff <= 2.0)
    print(f"2. Liczba osób ze stabilnymi wynikami (różnica <= 2%): {count_stable}")

    # 3. Podaj identyfikator osób (id_osoby), które osiągnęły trzy najwyższe 
    # średnie procentowe (średni procent oblicz jako średnia arytmetyczna ze wszystkich 
    # trzech testów danej osoby).
    sorted_by_avg = sorted(data, key=lambda x: x.avg_score, reverse=True)
    top_3 = sorted_by_avg[:3]
    
    print("3. Top 3 osoby (wg średniej):")
    for i, p in enumerate(top_3, 1):
        print(f"   #{i}: ID {p.id} (Średnia: {p.avg_score:.2f}%)")

    # 4. Znajdź osobę (osoby), których różnica między najniższym a 
    # najwyższym wynikiem procentowym jest największa.
    max_diff_global = max(p.diff for p in data)
    # Znajdujemy wszystkich, którzy mają taką różnicę na wypadek remisu
    most_inconsistent = [p for p in data if p.diff == max_diff_global]
    
    print(f"4. Największa różnica wyników ({max_diff_global:.2f}%):")
    for p in most_inconsistent:
        print(f"   -> ID {p.id} (Wyniki: {p.scores})")

if __name__ == "__main__":
    FILENAME = "dane.txt"
    dataset = parse_file(FILENAME)
    analyze_data(dataset)