import tkinter
from tkinter import *
from tkinter import ttk
from random import *
from Case import Case

# Create Tkinter Object
root = Tk()

# Set Geometry

# Frame 1

# Je l'ai fait en dehors de la classe pour tester, mais elle sera sûrement dedans
# le truc c'est que les w.createRectangle c'est des cases, et on a une classe case,
# donc je pense que il faut d'abord implémenter la classe case pour
# ensuite, au lieu de faire w.createRectangle, tout simplement créer un nouvel objet case à chaque
# case qu'on veut créer

cv = Canvas(root, height = 480, width = 480)
cv.pack()
root.update_idletasks()

for i in range(0, cv.winfo_height(), 10):
    for j in range(0, cv.winfo_width(), 10):
        c = Case(cv, i, j)


root.mainloop()


class Environnement:

    def __init__(self, nom, contenu, nbBatiments):
        self.nom = nom
        self.dimension = 48
        self.contenu = contenu
        self.nbBatiments = nbBatiments






