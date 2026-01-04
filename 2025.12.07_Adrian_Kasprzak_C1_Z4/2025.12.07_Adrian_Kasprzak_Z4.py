"""
Zadanie 4:
Na podstawie pliku 'oceny.txt' odpowiedz na pytania:
1. Ile jest przypadków braku ocen cząstkowych?
2. Ile indywidualnych studentów jest w pliku?
3. Ranking popularności przedmiotów.
4. Średnie semestralne słuchaczy.
5. Lista stypendystów.
"""

import sys
import os

INPUT_FILE = "oceny.txt"

# Słownik przedmiotów dla czytelności
SUBJECTS_MAP = {
    "mat": "Matematyka", "jpo": "Polski", "jan": "Angielski",
    "jhi": "Hiszpański", "hit": "Historia i Teraźniejszość", "bio": "Biologia",
    "fiz": "Fizyka", "che": "Chemia", "inf": "Informatyka",
    "wos": "WOS", "geo": "Geografia", "prz": "Przedsiębiorczość"
}

def school_round(number: float) -> int:
    """
    Standardowe zaokrąglanie arytmetyczne.
    """
    return int(number + 0.5)

def parse_data(filename):
    """
    Wczytuje plik i agreguje dane w strukturze słownika.
    """
    students = {}
    unclassified_cases = 0

    if not os.path.exists(filename):
        print(f"BŁĄD: Brak pliku {filename}!")
        return None, 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 2:
                continue # Pominiecie błędnych linii

            initials = parts[0]
            subj_code = parts[1]
            
            # Oceny tsą od indeksu 2 w górę
            grades = [int(g) for g in parts[2:]]
            
            # Zliczanie przypadków braku ocen
            if not grades:
                unclassified_cases += 1

            if initials not in students:
                students[initials] = {"subjects": {}}
            
            students[initials]["subjects"][subj_code] = grades

    return students, unclassified_cases

def analyze_students(students):
    """
    Przetwarza dane studentów: liczy średnie, sprawdza stypendia.
    """
    subject_popularity = {}
    student_averages = []
    scholarship_winners = []

    for initials, data in students.items():
        subjects_data = data["subjects"]
        
        # Popularność
        for subj in subjects_data.keys():
            subject_popularity[subj] = subject_popularity.get(subj, 0) + 1

        # Obliczanie ocen semestralnych
        semester_grades = []
        is_fully_classified = True
        
        for subj, grades in subjects_data.items():
            if not grades:
                is_fully_classified = False # Niesklasyfikowany z przedmiotu
                continue
            
            avg_partial = sum(grades) / len(grades)
            sem_grade = school_round(avg_partial)
            semester_grades.append(sem_grade)

        # Średnia studenta
        if semester_grades:
            final_average = sum(semester_grades) / len(semester_grades)
        else:
            final_average = 0.0

        student_averages.append((initials, final_average))

        # Stypendium
        # Warunki:
        # min 5 przedmiotów
        cond_a = len(subjects_data) >= 5
        # sklasyfikowany ze wszystkiego
        cond_b = is_fully_classified
        # każda ocena semestralna >= 3
        cond_c = all(g >= 3 for g in semester_grades) if semester_grades else False
        # średnia semestralna >= 4.00
        cond_d = final_average >= 4.00

        if cond_a and cond_b and cond_c and cond_d:
            scholarship_winners.append((initials, final_average))

    return subject_popularity, student_averages, scholarship_winners

def main():
    print("--- Zadanie 4: Analiza ocen ---")
    
    # Parsowanie
    students, unclassified_count = parse_data(INPUT_FILE)
    if not students:
        return

    # Analiza
    subj_pop, stud_avgs, winners = analyze_students(students)

    print(f"\n1. Niesklasyfikowani studenci: {unclassified_count}")

    print(f"\n2. Liczba aktywnych studentów: {len(students)}")

    print("\n3. Liczba słuchaczy na przedmiotach:")
    # Sortowanie malejąco wg liczby słuchaczy
    sorted_pop = sorted(subj_pop.items(), key=lambda x: x[1], reverse=True)
    for code, count in sorted_pop:
        full_name = SUBJECTS_MAP.get(code, code)
        print(f" - {full_name} ({code}): {count}")

    print("\n4. Średnie semestralne słuchaczy (Top 10):")
    # Sortowanie malejąco wg średniej
    sorted_avgs = sorted(stud_avgs, key=lambda x: x[1], reverse=True)
    for initials, avg in sorted_avgs[:10]:
        print(f" - {initials}: {avg:.2f}")
    if len(sorted_avgs) > 10:
        print("...reszta ukryta")

    print("\n5. STYPENDYŚCI :")
    # Sortowanie malejąco wg średniej
    sorted_winners = sorted(winners, key=lambda x: x[1], reverse=True)
    
    if not sorted_winners:
        print("BRAK. Nikt nie spełnił wyśrubowanych kryteriów.")
    else:
        for initials, avg in sorted_winners:
            print(f" - {initials} (Średnia: {avg:.2f})")

if __name__ == "__main__":
    main()