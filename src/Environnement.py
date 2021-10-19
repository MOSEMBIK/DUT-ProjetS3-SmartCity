from tkinter import *
from tkinter import ttk
from random import *
from src.Case import Case
# Create Tkinter Object
root = Tk()
min_room_size = 6
max_room_size = 20
max_rooms = 10
min_rooms = 3
max_iters = 3
palette = ["#927371", "#0a5a78"]



class Environnement:

    def __init__(self, nom):
        self.nom = nom
        self.canvas = Environnement.init_map(self)
        self.contenu = []

    def  init_map(self):
        cv = Canvas(root, height = 600, width = 600)
        cv.pack()
        root.update_idletasks()
        for i in range(0, cv.winfo_height(), 20):
            for j in range(0, cv.winfo_width(), 20):
                Case(cv, i, j, palette[0])
        return cv

    def init_rooms(self):
        # Choix aléatoire des coordonnées X et Y
        x = randrange(0, self.canvas.winfo_width() - 100, 20)
        y = randrange(0, self.canvas.winfo_height() - 100, 20)

        # De X jusqu'a la taille max de la room
        for i in range(x, x+100, 20):
            for j in range(y, y+100, 20):
                Case(self.canvas, i, j, palette[1])
                self.contenu.append()

    def main_loop(self):
        root.mainloop()


    def check_for_overlap(self, x, y):
