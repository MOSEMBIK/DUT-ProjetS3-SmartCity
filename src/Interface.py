import tkinter
import tkinter.ttk
from tkinter import *
from PIL import ImageTk, Image
import os
import tkinter.font as tkFont


# root = Tk()
# root1 = tkinter.Tk()
def addText(text, frame):
    font = tkFont.Font(family='Verdana', size=36, weight='bold')
    label = tkinter.Label(
        frame, text=text, font=font, justify='center'
    )
    label.place(anchor='nw', relx=0.25)


def addScore(score, frame):
    font = tkFont.Font(family='Verdana', size=36, weight='bold')
    label = tkinter.Label(
        frame, text=score, font=font, justify='center'
    )
    label.place(anchor='nw', relx=0.25, rely=0.25)


def addBoard(game_frame, agents):
    my_game = tkinter.ttk.Treeview(game_frame)
    my_game['columns'] = ('agent_id', 'autonomie', 'trajet', 'score')

    my_game.column("#0", width=0, stretch=NO)
    my_game.column("agent_id", anchor=CENTER, width=80)
    my_game.column("autonomie", anchor=CENTER, width=80)
    my_game.column("trajet", anchor=CENTER, width=80)
    my_game.column("score", anchor=CENTER, width=80)

    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("agent_id", text="Agent", anchor=CENTER)
    my_game.heading("autonomie", text="Charge", anchor=CENTER)
    my_game.heading("trajet", text="Trajet", anchor=CENTER)
    my_game.heading("score", text="score", anchor=CENTER)

    for i in agents.keys():
        agent = agents[i]

        my_game.insert(parent='', index='end', iid=agent.id, text='',
                       values=(agent.id, agent.charge, agent.caseOfTrajet, agent.score))

    my_game.place(anchor='nw', width=320, rely=0.1)
    return my_game

    # def updateBoard(selfself, column):


def updateTab(my_game, agent):
    children = my_game.get_children()
    my_game.delete(agent.id)
    my_game.insert(parent='', index=agent.id, iid=agent.id, text='',
                   values=(agent.id, agent.charge, agent.trajet[-1].getCoords(), agent.score))
    return my_game


def getScore(my_game):
    children = my_game.get_children()
    score = 0
    for i in children:
        score += my_game.item(i)['values'][3]
    return score


def createScoreValue(frame, score):
    font = tkFont.Font(family='Verdana', size=36)
    label = tkinter.Label(
        frame, text=score, justify='left', font=font
    )
    label.place(anchor='nw', relx=0.24, rely=0.05)
    return label


def updateScoreValue(label, score):
    label.config(text=score)


class Interface:
    def __init__(self, img):
        self.root = Tk()
        self.img = Image.open('img/' + img, 'r').convert('RGB')

    def getPx(self):
        """
        récupère un tableau de chaque pixel de l'image donnée en paramètre
        :return: liste de tous les pixels
        """
        return self.img.load()

    def createCanvas(self):
        w_image, h_image = self.img.size
        self.root.geometry('1600x' + str(h_image * 20))
        cv = Canvas(self.root, height=h_image * 20, width=w_image * 20)
        cv.grid(row=0, column=1, columnspan=1, sticky="N")

        # self.root.grid_columnconfigure(0, weight=1)
        # self.root.grid_columnconfigure(3, weight=1)
        # self.root.update_idletasks()
        cv.update()
        return cv

    @staticmethod
    def createLieu(cv, coordX, coordY, color):
        cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill=color, width=1, outline='#0b181c')

    @staticmethod
    def createRoad(cv, coordX, coordY):
        cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill='#efe4c6', width=1, outline='#967979')

    @staticmethod
    def createDecor(cv, coordX, coordY):
        cv.create_rectangle(coordX, coordY, coordX + 20, coordY + 20, fill='#000000', width=1)

    def main_loop(self):
        """
        Fonction tkinter qui garde la fenêtre active
        :return: void
        """
        self.root.mainloop()

    def createImg(self, cv, coords, equipe):
        if equipe == 0:
            skin = cv.create_oval(coords[0] * 20, coords[1] * 20, (coords[0] + 1) * 20, (coords[1] + 1) * 20, fill='green')
        else:
            skin = cv.create_oval(coords[0] * 20, coords[1] * 20, (coords[0] + 1) * 20, (coords[1] + 1) * 20, fill='red')

        # cv.create_rectangle(500, 500, 800, 800, fill='white')
        # cv.update()
        return skin

    @staticmethod
    def getPalette():
        palette = {'epicerie': '#b07678', 'magasin': '#00edd9', 'charge': '#1e736e', 'restaurant': '#8e00ed',
                   'ecole': '#5741b0', 'entrepot': '#a0be0e', 'cimetiere': '#5bc944', 'musee': '#ffe900',
                   'boulangerie': '#ed00c5', 'coiffeur': '#ec1c1a', 'pharmacie': '#6da6b7', 'spawn': '#ee8438'}

        return palette

    @staticmethod
    def imageMove(cv: Canvas, id, coords):
        # cv.tag_raise(id)
        resetCoords = cv.coords(id)
        cv.move(id, - resetCoords[0], - resetCoords[1])
        cv.move(id, coords[0] * 20, coords[1] * 20)

    def skins_map_update(self, cv: Canvas, mapS, skins):
        if mapS:
            cv.delete(mapS)
        im = Image.open('img/fond_route.png')
        imdec = Image.open('img/decor.png')
        h, w = self.img.size
        nim = im.resize((h * 20, w * 20), Image.ANTIALIAS)
        nimdec = imdec.resize((h * 20, w * 20), Image.ANTIALIAS)
        im = ImageTk.PhotoImage(nim)
        imdec = ImageTk.PhotoImage(nimdec)

        mapS = cv.create_image(0, 0, image=im, anchor=NW, disabledimage=im)

        if skins:
            for i in range(len(skins)):
                cv.tag_raise(skins[i])

        mapS = cv.create_image(0, 0, image=imdec, anchor=NW, disabledimage=im)

        # cv.create_rectangle(0, 0, h*20, w*20, fill='white')
        cv.update()
        return mapS

    def createIcon(self, icon):
        t = PhotoImage(file=icon)
        self.root.tk.call('wm', 'iconphoto', '.', t)

    def getWidth(self):
        return self.img.size

    def addFrame(self, column):
        game_frame = Frame(self.root, width=320, height=1600)
        game_frame.grid(row=0, column=column)

        return game_frame
