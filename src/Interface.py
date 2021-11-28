import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os



# root = Tk()
# root1 = tkinter.Tk()
class Interface:
    def __init__(self, img):
        self.root = Tk()
        self.img = Image.open('img/' + img, 'r').convert('RGB')

    def getPx(self):
        """
        récupère un tableau de chaque pixel de l'image donnée en paramètre
        :return: liste de tous les pixels
        """
        return self.img.load()

    def createCanvas(self):
        w_image, h_image = self.img.size
        cv = Canvas(self.root, height=h_image * 20, width=w_image * 20)
        cv.pack()
        self.root.update_idletasks()
        cv.update()
        return cv

    @staticmethod
    def createLieu(cv, coordX, coordY, color):
       cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill=color, width=1, outline='#0b181c')

    @staticmethod
    def createRoad(cv, coordX, coordY):
        cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill='#efe4c6', width=1, outline='#967979')

    @staticmethod
    def createDecor(cv, coordX, coordY):
        cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill='#000000', width=1)

    def main_loop(self):
        """
        Fonction tkinter qui garde la fenêtre active
        :return: void
        """
        self.root.mainloop()

    def createImg(self, cv, coords):
        skin = cv.create_oval(coords[0] * 20, coords[1] * 20, (coords[0]+1)*20, (coords[1]+1)*20, fill='green')
        #cv.create_rectangle(500, 500, 800, 800, fill='white')
        #cv.update()
        return skin

    @staticmethod
    def getPalette():
        palette = {'epicerie': '#b07678', 'magasin': '#00edd9', 'charge': '#1e736e', 'restaurant': '#8e00ed',
                   'ecole': '#5741b0', 'entrepot': '#a0be0e', 'cimetiere': '#5bc944', 'musee': '#ffe900',
                   'boulangerie': '#ed00c5', 'coiffeur': '#ec1c1a', 'pharmacie': '#6da6b7', 'spawn': '#ee8438'}

        return palette

    @staticmethod
    def imageMove(cv : Canvas, id, coords):
        cv.tag_raise(id)
        resetCoords = cv.coords(id)
        cv.move(id, - resetCoords[0], - resetCoords[1])
        cv.move(id, coords[0] * 20, coords[1] * 20)

    def skins_map_update(self, cv : Canvas, mapS, skins):
        if mapS :
            cv.delete(mapS)
        im = Image.open('img/newMapSkin.png')
        h, w = self.img.size
        nim = im.resize((h*20, w*20), Image.ANTIALIAS)
        im = ImageTk.PhotoImage(nim)

        mapS = cv.create_image(0, 0, image=im, anchor=NW, disabledimage=im)

        if skins :
            for i in range(len(skins)):
                cv.tag_raise(skins[i])

        #cv.create_rectangle(0, 0, h*20, w*20, fill='white')
        cv.update()
        return mapS


