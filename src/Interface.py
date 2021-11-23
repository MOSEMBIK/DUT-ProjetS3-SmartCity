import tkinter
from tkinter import *
from PIL import ImageTk, Image


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

    def createImg(self, cv, img):
        im = Image.open('img/' + img)
        im = ImageTk.PhotoImage(im)
        cv.pack()
        self.root.update_idletasks()
        cv.update()
        return cv.create_image(10 * 20, 7 * 20, image = im, anchor = NW)

    @staticmethod
    def getPalette():
        palette = {'epicerie': '#b07678', 'magasin': '#00edd9', 'charge': '#1e736e', 'restaurant': '#8e00ed',
                   'ecole': '#5741b0', 'entrepot': '#a0be0e', 'cimetiere': '#5bc944', 'musee': '#ffe900',
                   'boulangerie': '#ed00c5', 'coiffeur': '#ec1c1a', 'pharmacie': '#6da6b7', 'spawn': '#ee8438'}

        return palette
