import tkinter
from tkinter import *
from tkinter import ttk
from random import *


class Case:
    def __init__(self, cv, coordX, coordY):
        self.cv = cv
        if coordX < 0 or coordY < 0 or coordX > cv.winfo_width() or coordY > cv.winfo_width():
            print(cv.winfo_width())
            raise ValueError
        else:
            self.coordX = coordX
            self.coordY = coordY

            cv.create_rectangle(coordX, coordY, coordX+10, coordY+10, fill = 'blue')

    def getCoordonnees(self):
        return [self.coordX, self.coordY]