import math
import matplotlib.pyplot as plt
import numpy as np

def simulate_projectile_motion() -> None:
    g = 9.81  # Przyspieszenie ziemskie [m/s^2]
    
    print("--- SYMULATOR RZUTU UKOŚNEGO ---")
    print("Dodawaj kolejne rzuty. Aby zakończyć i narysować wykres, wpisz 'plot' lub 'q' zamiast prędkości.")

    simulations = [] # Lista do przechowywania parametrów

    # Pętla zbierania danych
    while True:
        print(f"\n--- Rzut nr {len(simulations) + 1} ---")
        v_input = input("Prędkość początkowa (m/s) [lub 'plot']: ").strip().lower()
        
        if v_input in ['plot', 'q', 'quit', 'exit', 'koniec']:
            if not simulations:
                print("Nie wprowadzono żadnych danych. Kończę.")
                return
            break
        
        try:
            v0 = float(v_input)
            if v0 < 0:
                print("Prędkość nie może być ujemna.")
                continue

            angle_input = input("Kąt rzutu (stopnie): ").strip()
            theta_deg = float(angle_input)
            
            if not (0 < theta_deg < 90):
                print("Dla rzutu ukośnego kąt powinien być między 0 a 90 stopni.")
                continue

            simulations.append((v0, theta_deg))
            print("Dodano do kolejki.")

        except ValueError:
            print("BŁĄD: Wpisz liczbę.")

    # Obliczenia i Rysowanie
    print(f"\nGeneruję wykres dla {len(simulations)} trajektorii...")
    plt.figure(figsize=(12, 7))

    for idx, (v0, theta_deg) in enumerate(simulations, 1):
        theta_rad = math.radians(theta_deg)

        # Fizyka - czas lotu: T = 2*v0*sin(theta) / g
        t_flight = (2 * v0 * math.sin(theta_rad)) / g
        
        # Generowanie punktów czasu (0 do t_flight, 200 punktów)
        t = np.linspace(0, t_flight, num=200)

        # Równania ruchu 
        # x(t) = v0 * cos(theta) * t
        x = v0 * math.cos(theta_rad) * t
        # y(t) = v0 * sin(theta) * t - 0.5 * g * t^2
        y = v0 * math.sin(theta_rad) * t - 0.5 * g * t**2

            # Statystyki (analityczne, dla dokładności)
        # Zasięg
        max_dist = x[-1] 
        # Wysokość (wierzchołek paraboli)
        max_height = (v0**2 * (math.sin(theta_rad)**2)) / (2 * g)

        print(f"Rzut {idx}: v={v0} m/s, kąt={theta_deg} stopni -> Zasięg: {max_dist:.2f}m, Max Wys.: {max_height:.2f}m")

        # Rysowanie linii
        plt.plot(x, y, label=f'#{idx}: v={v0}, $\\alpha$={theta_deg}°')

    # Kosmetyka wykresu
    plt.title("Porównanie trajektorii rzutów ukośnych")
    plt.xlabel("Dystans [m]")
    plt.ylabel("Wysokość [m]")
    plt.axhline(0, color='black', linewidth=1) # Ziemia
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    # Wymuszenie proporcji osi, żeby parabola nie była "zgnieciona"
    plt.axis('equal')
    # Ustawienie dołu wykresu na 0 (żeby nie uciekało pod ziemię przez błędy numeryczne)
    plt.ylim(bottom=0)
    
    plt.show()

if __name__ == "__main__":
    try:
        simulate_projectile_motion()
    except KeyboardInterrupt:
        print("\nPrzerwano przez użytkownika.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")