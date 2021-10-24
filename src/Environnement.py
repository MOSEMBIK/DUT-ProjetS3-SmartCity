import asyncio
import math
import tkinter
from tkinter import *
from random import *
from src.Lieu import *
from src.Case import *
import os
from PIL import ImageTk, Image

# Create Tkinter Object
root = Tk()
print(os.getcwd())
print(os.listdir())
img = ImageTk.PhotoImage(file="img/war.png")
palette = ["#927371", "#065d75"]
# Set Geometry

# Frame 1

class Environnement:

    def __init__(self, nom, nbBatiments):
        self.nom = nom
        self.contenu = {}
        self.canvas = Environnement.init_map(self)

    def  init_map(self):
        root.title(self.nom)
        cv = Canvas(root, height = 600, width = 600)
        cv.pack()
        root.update_idletasks()
        cv.update()
        for x in range(0, cv.winfo_height(), 20):
            for y in range(0, cv.winfo_width(), 20):
                Case(cv, x, y, palette[0])
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
                Case(self.canvas, i, j, palette[1])
                array_coords.append((i,j))
        # Ajoute a la location du lieu les coordonnées de chaque case
        self.contenu[id].setLocation(array_coords)

    # Simple fonction qui permet de garder la fenêtre active
    def main_loop(self):
        root.mainloop()

    def getContenu(self):
        return self.contenu

    def test_image(self):
        print(self.canvas.create_image(20, 20, image=img))
        self.canvas.addtag_above("oui", 1012)
        print(self.canvas.type(1011))

    # def check_for_overlap(self, x, y):




