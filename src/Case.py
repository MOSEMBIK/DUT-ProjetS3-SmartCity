import tkinter
from tkinter import *
from tkinter import ttk
from random import *


class Case:
    def __init__(self, cv, coordX, coordY, color):
        self.cv = cv
        if coordX < 0 or coordY < 0 or coordX > cv.winfo_width() or coordY > cv.winfo_width():
            raise ValueError
        else:
            self.coordX = coordX
            self.coordY = coordY
        if color != "#927371":
            cv.create_rectangle(coordX, coordY, coordX+20, coordY+20, fill = color)
        else:
            cv.create_rectangle(coordX, coordY, coordX+20, coordY+20, fill = color, outline = "#8d6e6d")


    def getCoordonnees(self):
        return [self.coordX, self.coordY]