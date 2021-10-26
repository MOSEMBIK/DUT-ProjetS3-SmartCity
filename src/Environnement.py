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
        # On initialise le canvas
        root.title(self.nom)
        cv = Canvas(root, height = h_image*20, width = w_image*20)
        cv.pack()
        root.update_idletasks()
        cv.update()

        # i,j boucle sur les pixels

        # ix, iy boucle sur la taille ajustée des cases
        ix = 0
        iy = 0
        for i in range(h_image):
            ix = 0
            for j in range(w_image):
                x = px[i, j]
                col = '#{:02x}{:02x}{:02x}'.format(*x)
                c = Case(cv, iy, ix, col)
                ix += 20
            iy += 20
        return cv


  #  def init_lieu():
    #    i = 0
     #   while i <  h_image:
      #      j = 0
       #     while j < w_image:

   # def get_taille_lieu(self, x, y):
   #     i = x
   #     j = y
    #    while px[i,j] == px[i+1, j]:



    """

    def getContenu(self):
        return self.contenu
        
    """

    def deplacement(self):
        def key_right(event):
            print(self.canvas.coords(self.img)[0])
            if self.canvas.coords(self.img)[0] > w_image*20:
                self.canvas.move(self.img, -w_image * 20 , 0)
            else:
                self.canvas.move(self.img, 20, 0)


        def key_left(event):
            if self.canvas.coords(self.img)[0] <= 0:
                self.canvas.move(self.img, w_image*20 - 20, 0)
            else:
                self.canvas.move(self.img, -20, 0)

        def key_up(event):
            self.canvas.move(self.img, 0, -20)

        def key_down(event):
            self.canvas.move(self.img, 0, 20)

        root.bind('<a>', key_left)
        root.bind('<w>', key_up)
        root.bind('<s>', key_down)
        root.bind('<d>', key_right)


    def main_loop(self):
        root.mainloop()


    def test_image(self):
        self.img = self.canvas.create_image(10*20, 7*20, image=img, anchor=NW)













