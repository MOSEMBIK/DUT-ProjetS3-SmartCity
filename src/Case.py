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
        """
        Constructeur de la case, créer un objet rectangle sur le canvas
        :param cv: canvas sur lequel on ajoute les rectangles
        :param coordX: Coordonnée X haut gauche du rectangle
        :param coordY:  Coordonné Y haut gauche du rectangle
        :param color: Couleur du rectangle
        """
        self.cv = cv
        """" Type de la case (spawn, route, epicerie, etc...)"""
        self.type = ''
        self.color = color
        if coordX < 0 or coordY < 0 or coordX > cv.winfo_width() or coordY > cv.winfo_width():
            raise ValueError("Coordonnées invalides")
        else:
            self.coordX = coordX
            self.coordY = coordY
        # Batiment
        if color in palette.values():
            cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill=color, width=1, outline='#0b181c')
            # Recupere la key associe a la couleur
            key = [k for k, v in palette.items() if v == color]
            # ajoute le tag
            self.type = ''.join(key)
        # Route
        elif color == '#efe4c6' or color == '#ffdfbe':
            cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill=color, width=1, outline='#967979')
            self.type = 'road'
        # Decor
        elif color == '#000000':
            cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill=color, width=1)
            self.type = 'decor'
        else:
            raise ValueError("La couleur n'existe pas dans le canvas")

    def getCoords(self):
        """
        Retourne les coordonnées en pixel de la case
        :return:
        """
        return [self.coordX / 20, self.coordY / 20]

    def getColor(self) -> str:
        """
        Getter sur la couleur de la case
        :return: string, couleur hexadecimal de la case
        """
        return self.color

    def isReachable(self) -> bool:
        """
        ! INCOMPLET !, vérifie seulement les routes
        :return: bool, true si la case est accessible, false sinon
        """
        return self.color == '#e1c183' or self.color == '#ffdfbe'

    def getType(self) -> str:
        """
        Recupere le type de la case
        :return:str, type de la case
        """
        return self.type

    def setPorte(self) -> None:
        return None
