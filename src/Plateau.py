import random as rd
from src.Interface import *
from src.Case import *


class Plateau:

    def __init__(self, nom):
        """
        Constructeur
        self.nom : Nom de la fenêtre
        self.contenu : Liste de toutes les cases créées.
        self.canvas : Canvas, objet tkinter, appelle la fonction init_map pour initialiser
        self.img : ID TKINTER (voir doc canvas tkinter) de l'image
        :param nom: Nom de la fenetre
        """
        self.nom = nom
        self.itf = Interface('newMap.png')
        self.contenu = []
        self.canvas = Plateau.init_map(self)
        self.img = 0

    def init_map(self):
        """
        Initialisation de la map,
        création d'une case à chaque couleur du canvas et l'ajoute à self.contenu
        :return: canvas crée
        """
        # On initialise le canvas
        self.itf.root.title(self.nom)
        cv = self.itf.createCanvas()
        px = self.itf.getPx()
        w_image, h_image = self.itf.img.size

        # ix, iy boucle sur la taille ajustée des cases
        iy = 0
        for i in range(h_image):
            ix = 0
            for j in range(w_image):
                x = px[j, i]
                col = '#{:02x}{:02x}{:02x}'.format(*x)
                c = Case(cv, ix, iy, col)
                self.contenu.append(c)
                ix += 20
            iy += 20
        return cv

    def main_loop(self):
        self.itf.main_loop()

    def test_image(self):
        self.img = self.itf.createImg(self.canvas, 'war.png')

    def getLieu(self, lieu):
        """
        Fonction qui recupère l'ensemble des cases ayant le type donné en paramètre
        :param lieu: lieu recherché (epicerie, magasin, charge, spawn)
        :return: liste de case appartenant a ce lieu
        """
        tab = []
        for case in self.contenu:
            if case.getType() == lieu:
                tab.append(case)
        return tab

    def getCase(self, coordX, coordY):
        """
        Fonction qui récupère la case de coordonnées X,Y (en pixel)
        :param coordX:  Coordonnés X en pixel de la case recherchée
        :param coordY: Coordonnées Y en pixel de la case recherchée
        :return: Case de coordonnée X,Y
        """
        for case in self.contenu:
            try:
                if case.getCoords() == [coordX, coordY]:
                    return case
            except:
                raise Exception("Invalid coords, case not found")

    def nearRoads(self, case: Case):
        """
        Récupère les routes adjacentes à la case donnée en paramètre
        :param case: Case dont on cherche les routes adjacentes
        :return: Liste de case adjacentes à la case donnée en paramètre
        """
        w_image, h_image = self.itf.img.size
        tab = []
        cases = []
        coords = case.getCoords()
        for i in range(-1, 2, 2):
            if 0 <= coords[0] + i < w_image:
                cases.append(self.getCase(coords[0] + i, coords[1]))
            if 0 <= coords[1] + i < h_image:
                cases.append(self.getCase(coords[0], coords[1] + i))
        for k in cases:
            if k.getType() == 'road':
                tab.append(k)
        return tab

    def setPortes(self):
        potentialPorte = []
        lieux = Interface.getPalette()
        lieux = [k for k, v in palette.items()]
        for lieu in lieux:
            casinas = self.getLieu('cimetiere')
            for case in casinas:
                if self.nearRoads(case):
                    potentialPorte.append(case)
        nouvellePorte = rd.choice(potentialPorte)
        nouvellePorte.setReachable()
        return nouvellePorte

    def nearLieu(self, case: Case):
        w_img, h_img = self.itf.img.size
        tablo = []
        cases = []
        coords = case.getCoords()
        for i in range(-1, 2, 2):
            if 0 <= coords[0] + i < w_img:
                cases.append(self.getCase(coords[0] + i, coords[1]))
            if 0 <= coords[1] + i < h_img:
                cases.append(self.getCase(coords[0], coords[1] + i))
        for k in cases:
            if k.isReachable() and k.getType() != 'road':
                tablo.append(k)
        return tablo
