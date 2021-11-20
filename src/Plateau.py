import tkinter
from tkinter import *

from src.Case import *
from PIL import ImageTk, Image

# Create Tkinter Object
#root = Tk()
#root1 = tkinter.Tk()
#im = Image.open('img/newMap.png', 'r').convert('RGB')
# px = im.load()
#img = Image.open('img/war.png')
#img = ImageTk.PhotoImage(img)
#palette = ['#5741b0', '#6da6b7', '#ec1c1a', '#ee8438', '#a0be0e', '#1e736e', '#5bc944']


# Frame 1

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
        print("OUE")
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
        print(h_image, w_image)
        for i in range(h_image):
            ix = 0
            for j in range(w_image):
                x = px[j, i]
                print(x)
                col = '#{:02x}{:02x}{:02x}'.format(*x)
                c = Case(cv, ix, iy, col)
                self.contenu.append(c)
                ix += 20
            iy += 20
        return cv
    """
    def deplacement(self):
        w_image, h_image = self.itf.img.size

        
        Fonction useless pour deplacer l'image car c'est rigolo
        :return:
        
        def key_right(event):
            print(self.canvas.coords(self.img)[0])
            if self.canvas.coords(self.img)[0] > w_image * 20:
                self.canvas.move(self.img, -w_image * 20, 0)
            else:
                self.canvas.move(self.img, 20, 0)

        def key_left(event):
            if self.canvas.coords(self.img)[0] <= 0:
                self.canvas.move(self.img, w_image * 20 - 20, 0)

            else:
                self.canvas.move(self.img, -20, 0)

        def key_up(event):
            self.canvas.move(self.img, 0, -20)

        def key_down(event):
            self.canvas.move(self.img, 0, 20)

        self.itf.root.bind('<a>', key_left)
        self.itf.root.bind('<w>', key_up)
        self.itf.root.bind('<s>', key_down)
        self.itf.root.bind('<d>', key_right)
    """

    def main_loop(self):
        self.itf.main_loop()

    #def test_image(self):
    #    """
     #   Initialisation de l'image sur le canvas et association de self.img
      #  :return:
       # """
        #self.img = self.canvas.create_image(10 * 20, 7 * 20, image=self.img, anchor=NW)

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

    def nearRoads(self, case : Case):
        """
        Récupère les routes adjacentes à la case donnée en paramètre
        :param case: Case dont on cherche les routes adjacentes
        :return: Liste de case adjacentes à la case donnée en paramètre
        """
        tab = [Case]
        cases = []
        coords = case.getCoords()
        for i in range(-1, 2, 2):
            cases.append(self.getCase(coords[0] + i, coords[1]))
            cases.append(self.getCase(coords[0], coords[1] + i))
        for k in cases:
            if k.getType() == 'road':
                tab.append(k)
        return tab







