"""
Zadanie Z5:
Program przetwarza plik 'wyniki.txt' zawierający statystyki agentów.
Realizuje 5 zadań analitycznych:
1. Podaj listę osób (nazwa/numer agenta) o 10 najlepszych wynikach z pływania.
2. Z którą umiejętnością agenci radzą sobie najlepiej (przeanalizuj arytmetyczną średnią punktów wszystkich agentów dla każ-
dej umiejętności)?
3. Wyświetl listę osób, które uzyskały najgorszy wynik z zakresu danej umiejętności (najgorszą osobę w pływaniu, najgorszą
osobę w strzelaniu itd.). Jeżeli najgorszy wynik w danej kategorii osiągnęło więcej osób, pokaż je wszystkie.
4. Przedstaw uporządkowane listy agentów od najlepszego do najgorszego dla wspinaczki, hakowania i wiedzy.
5. Przyjmij, że inteligencja wpływa na tempo rozwoju takich umiejętności jak hakowanie i wiedza. Inteligencja jest niezmienna.
Każde 10 punktów inteligencji powoduje rokroczny wzrost hakowania i wiedzy agenta o 1 punkt. Przykładowo: dla inteligen-
cji wynoszącej 24 punkty, hakowanie i wiedza wzrosną po roku każda o 2 punkty. Ile wyniesie hakowanie każdego z agentów
w 2030 roku? Na ile punktów zostanie obliczona wiedza agentów w 2040 roku?
"""

import os
import math

def load_agents(filename):
    agents = []
    if not os.path.exists(filename):
        print(f"BŁĄD: Nie znaleziono pliku '{filename}'.")
        return []

    print(f"Wczytuję bazę danych agentów z: {filename}...")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Pobranie nagłówków
            header_line = f.readline().strip()
            if not header_line:
                return []
            
            headers = [h.strip() for h in header_line.split(',')]
            
            # Parsowanie wierszy
            for line in f:
                line = line.strip()
                if not line: continue
                
                parts = line.split(',')
                
                # Walidacja długości
                if len(parts) != len(headers):
                    continue

                agent_data = {}
                # Pierwsza kolumna to nazwa agenta-string, reszta to liczby-int
                agent_data['name'] = parts[0].strip()
                
                for i in range(1, len(headers)):
                    category = headers[i]
                    try:
                        agent_data[category] = int(parts[i])
                    except ValueError:
                        agent_data[category] = 0 # Fallback przy błędnych danych

                agents.append(agent_data)

    except Exception as e:
        print(f"BŁĄD KRYTYCZNY: {e}")
        return []

    return agents, headers[1:] # Zwracamy dane i listę kategorii bez agenta

def analyze_agents(agents, categories):
    if not agents:
        print("Brak danych.")
        return

    print(f"\nZAŁADOWANO: {len(agents)} akt osobowych.\n")

    # 1: Top 10 Pływanie
    print("1. Top 10 Pływanie")
    # Sortowanie malejąco wg kategorii 'pływanie'
    swimmers = sorted(agents, key=lambda x: x.get('pływanie', 0), reverse=True)
    for i, agent in enumerate(swimmers[:10], 1):
        print(f"{i}. {agent['name']}: {agent['pływanie']} pkt")

    # 2: Najłatwiejsza umiejętność
    print("\n2. Najłatwiejsza umiejętność")
    best_skill = ""
    max_avg = -1
    
    for cat in categories:
        total_score = sum(a.get(cat, 0) for a in agents)
        avg = total_score / len(agents)
        if avg > max_avg:
            max_avg = avg
            best_skill = cat
            
    print(f"Agenci najlepiej radzą sobie z: '{best_skill.upper()}'")
    print(f"Średni wynik globalny: {max_avg:.2f} pkt")

    # 3: Najgorsi w każdej kategorii
    print("\n3. Najgorsi w każdej kategorii")
    for cat in categories:
        # Znajdź minimum w danej kategorii
        min_score = min(a.get(cat, 0) for a in agents)
        # Obsługa remisu
        worst_agents = [a['name'] for a in agents if a.get(cat, 0) == min_score]
        
        worst_str = ", ".join(worst_agents)
        print(f"{cat.capitalize()} (Wynik: {min_score}): {worst_str}")

    # 4: Rankingi specyficzne
    print("\n4. Rankingi specyficzne")
    target_skills = ['wspinaczka', 'hakowanie', 'wiedza']
    
    for skill in target_skills:
        if skill not in categories:
            print(f"Brak danych dla: {skill}")
            continue
            
        print(f"\n4. Ranking: {skill.capitalize()}")
        sorted_agents = sorted(agents, key=lambda x: x.get(skill, 0), reverse=True)
        
        # Wyświetlamy tylko początek i koniec listy dla czytelności w konsoli
        for a in sorted_agents[:3]:
            print(f"   [TOP] {a['name']}: {a[skill]}")
        print("   ...")
        for a in sorted_agents[-3:]:
            print(f"   [BOT] {a['name']}: {a[skill]}")

    # 5: Symulacja 2030 i 2040
    print("\n5. Symulacja 2030 i 2040")
    print("Zasada: +1 pkt rozwoju za każde pełne 10 pkt Inteligencji / rok.")
    
    current_year = 2024
    target_hack = 2030
    target_know = 2040
    
    delta_hack = target_hack - current_year # 6 lat
    delta_know = target_know - current_year # 16 lat
    
    print(f"Horyzont czasowy: Hakowanie (+{delta_hack} lat), Wiedza (+{delta_know} lat)")
    print("-" * 50)
    print(f"{'AGENT':<12} | {'INTELIGENCJA':<12} | {'BONUS ROCZNY':<12} | {'HAKOWANIE 2030':<12} | {'WIEDZA 2040':<12}")
    print("-" * 50)
    
    for a in agents:
        intel = a.get('inteligencja', 0)
        # Dzielenie całkowite 
        yearly_growth = intel // 10
        
        base_hack = a.get('hakowanie', 0)
        base_know = a.get('wiedza', 0)
        
        future_hack = base_hack + (yearly_growth * delta_hack)
        future_know = base_know + (yearly_growth * delta_know)
        
        print(f"{a['name']:<12} | {intel:<12} | +{yearly_growth:<11} | {future_hack:<14} | {future_know:<12}")

if __name__ == "__main__":
    FILENAME = "wyniki.txt"
    data, cats = load_agents(FILENAME)
    analyze_agents(data, cats)