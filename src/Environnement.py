import asyncio
import math
import tkinter
from tkinter import *
import PIL.Image

from src.Lieu import *
from src.Case import *
import os
from PIL import ImageTk, Image
import random

# Create Tkinter Object
root = Tk()
root1 = tkinter.Tk()
im = Image.open('img/srcMAP.png', 'r').convert('RGB')
px = im.load()
img = Image.open('img/war.png')
img = ImageTk.PhotoImage(img)
palette = ['#5741b0', '#6da6b7', '#ec1c1a', '#ee8438', '#a0be0e', '#1e736e', '#5bc944']
w_image, h_image = im.size

# Frame 1

class Environnement:

    def __init__(self, nom):
        self.nom = nom
        self.contenu = {}
        self.canvas = Environnement.init_map(self)
        self.img = 0

    def init_map(self):
        root.title(self.nom)
        cv = Canvas(root, height = h_image*20, width = w_image*20)
        cv.pack()
        root.update_idletasks()
        cv.update()

        i = 0
        j = 0
        ix = 0
        iy = 0
        while i < h_image:
            j = 0
            ix = 0
            while j < w_image:
                x = px[i, j]
                col = '#{:02x}{:02x}{:02x}'.format(*x)
                c = Case(cv, iy, ix, col)
                j += 1
                ix += 20
            i += 1
            iy += 20
        return cv

    def main_loop(self):
        root.mainloop()
    """

    def getContenu(self):
        return self.contenu
        
    """

    def ok(self):
        def key_right(event):
            self.canvas.move(self.img, 20, 0)

        def key_left(event):
            self.canvas.move(self.img, -20, 0)
        root.bind('<d>', key_right)

        def key_up(event):
            self.canvas.move(self.img, 0, -20)

        def key_down(event):
            self.canvas.move(self.img, 0, 20)

        root.bind('<a>', key_left)
        root.bind('<w>', key_up)
        root.bind('<s>', key_down)







    def test_image(self):
        self.img = self.canvas.create_image(10*20, 7*20, image=img, anchor=NW)













