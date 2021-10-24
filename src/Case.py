from tkinter import *
from random import *


class Case:
    def __init__(self, cv, coordX, coordY, color):
        self.cv = cv
        self.id = 0
        if coordX < 0 or coordY < 0 or coordX > cv.winfo_width() or coordY > cv.winfo_width():
            raise ValueError
        else:
            self.coordX = coordX
            self.coordY = coordY
        if color != "#927371":
            self.id = cv.create_rectangle(coordX, coordY, coordX+20, coordY+20, fill = color)
        else:
            self.id = cv.create_rectangle(coordX, coordY, coordX+20, coordY+20, fill = color, outline = "#8d6e6d")


    def getCoordonnees(self):
        return [self.coordX, self.coordY]

    def getCanvasId(self):
        return self.id

