import time

INPUT_FILE = "dane_1.txt"
OUTPUT_FILE = "wyniki_c3.txt"

def remove_adjacent_duplicates(text: str) -> str:
    """
    Usuwa sąsiadujące duplikaty znaków (np. 'aa' -> 'a').
    Złożoność: O(n).
    """
    if not text:
        return ""

    result = [text[0]]
    
    for char in text[1:]:
        # Dodajemy znak tylko jeśli jest różny od ostatnio dodanego
        if char != result[-1]:
            result.append(char)
            
    return "".join(result)

def main():
    print("Ćwiczenie C3: Redukcja powtórzeń")

    try:
        # Wczytanie danych
        print(f"Wczytywanie: {INPUT_FILE}...")
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        if not lines:
            print("Błąd: Plik jest pusty.")
            return

        processed_lines = []
        
        # Przetwarzanie z pomiarem czasu
        start_time = time.perf_counter_ns()

        for line in lines:
            clean_line = remove_adjacent_duplicates(line)
            processed_lines.append(clean_line)

        end_time = time.perf_counter_ns()
        duration_us = (end_time - start_time) / 1000

        # Zapis wyników
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write("\n".join(processed_lines))

        # Raport
        print(f"Sukces. Przetworzono {len(lines)} linii.")
        print(f"Czas operacji: {duration_us:.4f} µs")
        print(f"Zapisano do: {OUTPUT_FILE}")
        
        # Podgląd dla pewności
        print("\n--- Podgląd (pierwsze 3 linie) ---")
        for i, line in enumerate(processed_lines[:3], 1):
            print(f"{i}: {line}")

    except FileNotFoundError:
        print(f"BŁĄD KRYTYCZNY: Nie znaleziono pliku '{INPUT_FILE}'.")
        print("Upewnij się, że plik znajduje się w tym samym katalogu co skrypt.")
    except Exception as e:
        print(f"Błąd niespodziewany: {e}")

if __name__ == "__main__":
    main()