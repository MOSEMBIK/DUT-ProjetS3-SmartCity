from tkinter import *
from random import *

palette = {}
palette['epicerie'] = '#b07678'
palette['magasin'] = '#00edd9'
palette['charge'] = '#1e736e'
palette['restaurant'] = '#8e00ed'
palette['ecole'] = '#5741b0'
palette['entrepot'] = '#a0be0e'
palette['cimetiere'] = '#5bc944'
palette['musee'] = '#ffe900'
palette['boulangerie'] = '#ed00c5'
palette['coiffeur'] = '#ec1c1a'
palette['pharmacie'] = '#6da6b7'
palette['spawn'] = '#ee8438'
'#ec1c1a'
# palette = ['#b07678', '#00edd9', '#1e736e', '#8e00ed', '#5741b0', '#ec1c1a', '#5bc944', '#ffe900', '#ed00c5',
# '#1e736e','#6da6b7', '#ee8438']


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
        if color in palette.values():
            c = cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill=color, width=1, outline='#0b181c')
            # Recupere la key associe a la couleur
            key = [k for k, v in palette.items() if v == color]
            # ajoute le tag
            self.type = ''.join(key)
        elif color == '#efe4c6' or color == '#ffdfbe':
            c = cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill=color, width=1, outline='#967979')
            self.type = 'road'
        elif color == '#000000':
            c = cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill=color, width=1)
            self.type = 'decor'
        else:
            c = cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill='purple', width=1)
            print(color)
            self.type = 'probleme'

    def getCoords(self):
        return [self.coordX/20, self.coordY/20]

    def getCanvasId(self):
        return self.id

    def getColor(self):
        return self.color

    def isReachable(self):
        return self.color == '#e1c183' or self.color == '#ffdfbe'

    def getType(self):
        return self.type

    def nearRoad(self):

        self.getCoords()
        for i in range(-1, 1, 2):
            for j in range(-1, 1, 2):
                print(i, j)
