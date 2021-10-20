import asyncio
import math

import tkinter
from tkinter import *
from tkinter import ttk
from random import *
from src.Lieu import *
# Create Tkinter Object
root = Tk()
palette = ["#927371", "#065d75"]
# Set Geometry

# Frame 1

# Je l'ai fait en dehors de la classe pour tester, mais elle sera sûrement dedans
# le truc c'est que les w.createRectangle c'est des cases, et on a une classe case,
# donc je pense que il faut d'abord implémenter la classe case pour
# ensuite, au lieu de faire w.createRectangle, tout simplement créer un nouvel objet case à chaque
# case qu'on veut créer


class Environnement:

    def __init__(self, nom, nbBatiments):
        self.nom = nom
        self.canvas = Environnement.init_map(self)
        self.contenu = {}

    def  init_map(self):
        root.title(self.nom)
        cv = Canvas(root, height = 600, width = 600)
        cv.pack()
        root.update_idletasks()
        cv.update()
        for x in range(0, cv.winfo_height(), 20):
            for y in range(0, cv.winfo_width(), 20):
                cv.create_rectangle(x, y, x + 20, y + 20, fill=palette[0], outline="#8d6e6d")
        return cv

    def init_rooms(self, id):

        # Choix aléatoire des coordonnées X et Y
        x = randrange(0, self.canvas.winfo_width() - 100, 20)
        y = randrange(0, self.canvas.winfo_height() - 100, 20)
        # if check_for_overlap():
        # Ajout du lieu au tableau
        self.contenu[id] = (Lieu(id, "Bleu"))
        array_coords = []
        # De X jusqu'a la taille max de la room
        for i in range(x, x+100, 20):
            for j in range(y, y+100, 20):
                c = self.canvas.create_rectangle(i, j, i + 20, j + 20, fill=palette[1])
                array_coords.append((i,j))
        # Ajoute a la location du lieu les coordonnées de chaque case
        self.contenu[id].setLocation(array_coords)

    # Simple fonction qui permet de garder la fenêtre active
    def main_loop(self):
        root.mainloop()

    def getContenu(self):
        return self.contenu

    #def check_for_overlap(self, x, y):
    #    for i in range(x, x+100, 20):
   #         for j in range(y, y+100, 20):
  #              for lieu in self.contenu:
 #                   for coords in lieu.getLocation()
#                    if i == lieu.getLocation()[0] || y == lieu.getLocation()[1])



