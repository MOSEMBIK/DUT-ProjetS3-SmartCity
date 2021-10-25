import asyncio
import math
import tkinter
from tkinter import *
from src.Lieu import *
from src.Case import *
import os
from PIL import Image as ImageTk
import random

# Create Tkinter Object
root = Tk()
img = ImageTk.PhotoImage(file="img/war.png")
palette = ["#927371", "#065d75"]
# Set Geometry

# Frame 1

class Environnement:

    def __init__(self, nom, dimensions):
        self.nom = nom
        self.dimensions = dimensions
        self.contenu = {}
        self.canvas = Environnement.init_map(self)

    def  init_map(self):
        root.title(self.nom)
        cv = Canvas(root, height = self.dimensions, width = self.dimensions)
        cv.pack()
        root.update_idletasks()
        cv.update()
        for x in range(0, cv.winfo_height(), 20):
            for y in range(0, cv.winfo_width(), 20):
                Case(cv, x, y, palette[0])
        return cv

    def init_rooms(self, id):
        lieu_valide = True

        # Choix aléatoire des coordonnées X et Y
        x = randrange(0, self.canvas.winfo_width() - 100, 20)
        y = randrange(0, self.canvas.winfo_height() - 100, 20)

        array_coords = []

        # De X jusqu'a la taille max de la room
        for i in range(x, x+100, 20):
            for j in range(y, y+100, 20):

                # Si la case est déjà prise par un autre lieu
                if not self.check_for_overlap(i, j):
                    # Lieu non valide, break loop
                    lieu_valide = False
                    break
                # Sinon, créer une case, lui associe un tag et l'ajoute au tableau de coordonnées du lieu.
                c = Case(self.canvas, i, j, palette[1])
                self.canvas.addtag_withtag("Lieu" + str(id), c.getCanvasId())
                array_coords.append(c)
            else:
                continue
            break
        if lieu_valide:
            self.contenu[id] = Lieu(id, "Lieu" + str(id))
            self.contenu[id].setLocation(array_coords)
            return True
        else:
            # Si le lieu n'est pas valide, supprime les cases du lieu avec le tag associé
            self.canvas.delete("Lieu" + str(id))
            return False

    def main_loop(self):
        """ Simple fonction qui permet de garder la fenêtre active"""
        root.mainloop()

    def getContenu(self):
        return self.contenu

    def test_image(self):
        self.canvas.create_image(20, 20, image=img, anchor=NW)


    def check_for_overlap(self, x, y):
        """Fonction aui prends en parametre les coordonnées d'une case
        Return true si cette case n'est pas prise par un autre lieu, false sinon"""
        case_valide = True
        # Si c'est le premier lieu que l'on crée return true
        if len(self.contenu) == 0:
            return True
        # Sinon check pour chaque case de chaque lieu si les coordonnées ne sont pas déjà pris
        for lieu in self.contenu:
            for coords in self.contenu[lieu].getLocation():
                if x == coords.getCoordonnees()[0] and y == coords.getCoordonnees()[1]:
                    case_valide = False
        return case_valide

    def connect_rooms(self):
        # Init
        lieuA = 0
        lieuB = 0
        for i in range(len(self.contenu)-1):
            lieuA = self.contenu[i]
            lieuB = self.contenu[i+1]

            lieuAloc = random.choice(lieuA.getLocation())
            lieuBloc = random.choice(lieuB.getLocation()).getCoordonnees()
            print(lieuAloc)

            for (x, y) in (lieuAloc.getCoordonnees(), lieuBloc.getCoordonnees()):
                miakhalifa = random.randint(0,1)
                print(x)
                print(y)
             #   if miakhalifa == 0:












