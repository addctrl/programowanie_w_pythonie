"""
ZADANIE Z3: 
Grafika rekurencyjna 
Program generuje fraktalny wzór kół za pomocą rekurencji.

ALGORYTM:
Dla zadanego obszaru (x, y, rozmiar):
1. Rysuje koło wpisane w ten obszar.
2. Dzieli obszar na 4 ćwiartki.
3. Wywołuje się rekurencyjnie dla każdej ćwiartki (z mniejszym rozmiarem).
Warunek stopu: osiągnięcie zadanej głębokości (depth == 0).
"""

import tkinter as tk

# Konfiguracja
WINDOW_SIZE = 600
INITIAL_DEPTH = 4  # Głębokość rekurencji

class RecursiveCirclesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("=== Z3: Rekurencyjne koła ===")
        
        # Panel sterowania
        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.TOP, pady=5)
        
        tk.Label(self.frame, text="Głębokość rekurencji:").pack(side=tk.LEFT)
        self.entry_depth = tk.Entry(self.frame, width=5)
        self.entry_depth.insert(0, str(INITIAL_DEPTH))
        self.entry_depth.pack(side=tk.LEFT, padx=5)
        
        tk.Button(self.frame, text="Rysuj", command=self.draw).pack(side=tk.LEFT)
        
        # Płótno
        self.canvas = tk.Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE, bg="white")
        self.canvas.pack()
        
        # Pierwsze rysowanie
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        try:
            depth = int(self.entry_depth.get())
        except ValueError:
            depth = INITIAL_DEPTH
            
        # Margines, żeby nie rysować przy samej krawędzi
        margin = 20
        size = WINDOW_SIZE - 2 * margin
        
        # Uruchomienie rekurencji
        # x, y to lewy górny róg obszaru
        self.draw_recursive(margin, margin, size, depth)

    def draw_recursive(self, x, y, size, depth):
        """
        Główna funkcja rekurencyjna.
        x, y: współrzędne lewego górnego rogu kwadratu
        size: bok kwadratu
        depth: licznik poziomów rekurencji
        """
        if depth == 0:
            return

        # Rysujemy koło wpisane w aktualny kwadrat
        self.canvas.create_oval(x, y, x + size, y + size, outline="black")

        # Obliczamy parametry dla mniejszych kwadratów (ćwiartek)
        half_size = size / 2
        new_depth = depth - 1
        
        # Wywołania rekurencyjne dla 4 ćwiartek:
        
        # 1. Lewa górna
        self.draw_recursive(x, y, half_size, new_depth)
        
        # 2. Prawa górna
        self.draw_recursive(x + half_size, y, half_size, new_depth)
        
        # 3. Lewa dolna
        self.draw_recursive(x, y + half_size, half_size, new_depth)
        
        # 4. Prawa dolna
        self.draw_recursive(x + half_size, y + half_size, half_size, new_depth)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecursiveCirclesApp(root)
    root.mainloop()