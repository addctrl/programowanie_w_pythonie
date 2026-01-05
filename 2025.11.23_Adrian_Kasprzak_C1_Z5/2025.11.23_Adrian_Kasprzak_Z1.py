import matplotlib.pyplot as plt
import numpy as np

def main():
    print("--- EDUKACYJNY GENERATOR PARABOL (NumPy Edition) ---")
    
    # Definicja danych 
    # Generujemy 500 punktów od razu dla wszystkich wykresów.
    x = np.linspace(-5, 5, 500)

    # Definicja 6 przypadków (a, b, c, Tytuł)
    # a - kierunek ramion, 
    # delta - liczba miejsc zerowych
    cases = [
        # Wiersz 1: a > 0 
        (1, 0, -4,  r"$a>0, \Delta>0$ (2 m. zerowe)"),  # x^2 - 4
        (1, 0, 0,   r"$a>0, \Delta=0$ (1 m. zerowe)"),   # x^2
        (1, 0, 2,   r"$a>0, \Delta<0$ (brak m. zerowych)"), # x^2 + 2
        
        # Wiersz 2: a < 0 
        (-1, 0, 4,  r"$a<0, \Delta>0$ (2 m. zerowe)"),  # -x^2 + 4
        (-1, 0, 0,  r"$a<0, \Delta=0$ (1 m. zerowe)"),   # -x^2
        (-1, 0, -2, r"$a<0, \Delta<0$ (brak m. zerowych)") # -x^2 - 2
    ]

    # Rysowanie
    fig, axs = plt.subplots(2, 3, figsize=(14, 8))
    fig.suptitle('Analiza rozwiązań równania kwadratowego $ax^2+bx+c=0$', fontsize=16)

    # Spłaszczamy tablicę osi dla łatwej iteracji
    axs_flat = axs.flatten()

    for ax, (a, b, c, title) in zip(axs_flat, cases):
        # Obliczenie Y - tutaj dzieje się magia NumPy.
        # Zamiast pętli for, mnożymy całą tablicę przez skalar.
        y = a * x**2 + b * x + c
        
        # Rysowanie
        ax.plot(x, y, linewidth=2.5, color='royalblue')
        
        # Osie układu
        ax.axhline(0, color='black', linewidth=1, zorder=1)
        ax.axvline(0, color='black', linewidth=1, zorder=1)
        
        # Kosmetyka
        ax.set_title(title, fontsize=11, fontweight='bold')
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Ustawienie sztywnych granic Y dla łatwego porównania wizualnego
        ax.set_ylim(-6, 6)
        ax.set_xlim(-5, 5)
        
        # Zaznaczenie miejsc zerowych 
        # Znajdujemy przybliżone miejsca zerowe numerycznie, tam gdzie znak zmienia się
        zero_crossings = np.where(np.diff(np.sign(y)))[0]
        if len(zero_crossings) > 0:
             ax.plot(x[zero_crossings], y[zero_crossings], 'ro', markersize=6, label='Miejsce zerowe')
             ax.legend(loc='upper right', fontsize='small')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()