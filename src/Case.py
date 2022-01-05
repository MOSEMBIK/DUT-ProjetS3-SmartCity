from random import *

from src import Interface
from src.Interface import *

palette = {'Bioserre': '#b07678', 'Accumulateurs électriques': '#00edd9', 'Chateau d\'eau': '#1e736e', 'Panneaux solaires': '#8e00ed',
           'Station de recyclage': '#5741b0', 'Centre de contrôle': '#a0be0e', 'Parc éolien': '#88877e', 'Centre météorologique': '#ffe900',
           'Entrepôt': '#ed00c5', 'Générateur d\'énergie': '#ec1c1a', 'Mine': '#6da6b7', 'Spawn': '#ee7490', 'Laboratoire': '#6a2a3a', 'Zone de recharge': '#5bc944'}




class Case:
    """
    Element du Plateau.
    """
    def __init__(self, cv, coordX, coordY, color):
        """
        Constructeur de la case, créer un objet rectangle sur le canvas
        :param cv: canvas sur lequel on ajoute les rectangles
        :param coordX: Coordonnée X haut gauche du rectangle
        :param coordY:  Coordonné Y haut gauche du rectangle
        :param color: Couleur du rectangle
        """
        self.cv = cv
        self.reachable = False
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
            Interface.createLieu(self.cv, self.coordX, self.coordY, color)
            # Recupere la key associe a la couleur
            key = [k for k, v in palette.items() if v == color]
            # ajoute le tag
            self.type = ''.join(key)
        # Route
        elif color == '#efe4c6':
            Interface.createRoad(self.cv, self.coordX, self.coordY)
            self.type = 'road'
            self.reachable = True
        # Decor
        elif color == '#000000':
            Interface.createDecor(self.cv, self.coordX, self.coordY)
            self.type = 'decor'
        else:
            raise ValueError(f"La couleur n'existe pas dans le canvas. X({coordX})Y({coordY})")

    def getCoords(self):
        """
        Retourne les coordonnées en pixel de la case
        :return:
        """
        return [self.coordX / 12, self.coordY / 12]

    def getColor(self) -> str:
        """
        Getter sur la couleur de la case
        :return: string, couleur hexadecimal de la case
        """
        return self.color

    def isReachable(self) -> bool:
        """
        :return: bool, true si la case est accessible, false sinon
        """
        return self.reachable

    def setReachable(self, reachable: bool = True):
        self.reachable = reachable

    def getType(self) -> str:
        """
        Recupere le type de la case
        :return:str, type de la case
        """
        return self.type

