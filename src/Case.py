from tkinter import *
from random import *

palette = ['#5741b0', '#6da6b7', '#ec1c1a', '#ee8438', '#a0be0e', '#1e736e', '#5bc944']
route = ''

class Case:
    def __init__(self, cv, coordX, coordY, color):
        self.cv = cv
        self.id = 0
        self.color = color
        if coordX < 0 or coordY < 0 or coordX > cv.winfo_width() or coordY > cv.winfo_width():
            raise ValueError
        else:
            self.coordX = coordX
            self.coordY = coordY
        if color in palette:
            c = cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill=color, width=1, outline='#0b181c')
            self.type = 'lieu'
            for color in palette:
                self.cv.addtag_withtag(color, c)
        elif color == '#efe4c6':
            c = cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill=color, width=1, outline='#967979')
            self.type = 'road'
        else:
            c = cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill=color, width=1, outline='#967979')
            self.type = 'decor'


    def getCoordonnees(self):
        return [self.coordX, self.coordY]

    def getCanvasId(self):
        return self.id

    def getColor(self):
        return self.color

    def isReachable(self):
        return self.color == 'e1c183'

    def getType(self):
        return self.type


