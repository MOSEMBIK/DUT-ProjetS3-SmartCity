import tkinter
import tkinter.ttk
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont

from src.Agent import *


# root = Tk()
# root1 = tkinter.Tk()
def addText(team, frame):
    font = tkFont.Font(family='Verdana', size=18, weight='bold')
    label = tkinter.Label(
        frame, text="Score :", font=font, justify='center'
    )
    label.place(anchor='nw', relx=0.65, rely=0.05)

    equipe = tkinter.Label(
        frame, text=team + " Team", font=font, justify='center'
    )
    equipe.place(anchor='nw', rely=0.01)


def addButton(frame, x, y, text):
    w = tkinter.Button(frame, text=text)
    w.place(anchor="nw", rely=x, relx=y)
    return w


def addBoard(game_frame, agents):
    style = tkinter.ttk.Style()
    style.configure("Treeview", font=('Calibri', 11))

    my_game = tkinter.ttk.Treeview(game_frame, style="Treeview")
    my_game['columns'] = ('agent_id', 'autonomie', 'position', 'score', 'tache', 'tacheAr', 'volume', 'Va charger')

    my_game.column("#0", width=0, stretch=NO)
    my_game.column("agent_id", anchor=CENTER, width=20)
    my_game.column("autonomie", anchor=CENTER, width=60)
    my_game.column("position", anchor=CENTER, width=60)
    my_game.column("score", anchor=CENTER, width=60)
    my_game.column("tache", anchor=CENTER, width=120)
    my_game.column("tacheAr", anchor=CENTER, width=120)
    my_game.column("volume", anchor=CENTER, width=60)
    my_game.column("Va charger", anchor=CENTER, width=60)

    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("agent_id", text="ID", anchor=CENTER)
    my_game.heading("autonomie", text="Charge", anchor=CENTER)
    my_game.heading("position", text="Position", anchor=CENTER)
    my_game.heading("score", text="score", anchor=CENTER)
    my_game.heading("tache", text="tache", anchor=CENTER)
    my_game.heading("tacheAr", text="tacheAr", anchor=CENTER)
    my_game.heading("volume", text="volume", anchor=CENTER)
    my_game.heading("Va charger", text="Va charger", anchor=CENTER)

    for i in agents.keys():
        agent: Agent = agents[i]

        my_game.insert(parent='', index='end', iid=agent.id, text='',
                       values=(agent.id,
                               agent.charge / agent.autonomie * 100,
                               0,
                               agent.score,
                               "No task",
                               "No task",
                               0, '-'))

    my_game.place(anchor='nw', width=860, height=140, rely=0.3)
    return my_game

    # def updateBoard(selfself, column):


def createWinnerTeamTab(game_frame):
    my_game = tkinter.ttk.Treeview(game_frame, style="Treeview")
    my_game['columns'] = 'Equipe'

    my_game.column("#0", width=0, stretch=NO)
    my_game.column("Equipe", anchor=CENTER, width=60)

    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("Equipe", text="Equipe Gagnante", anchor=CENTER)

    my_game.insert(parent='', index='end', iid='BLUE TEAM', text='',
                   values='-')

    my_game.insert(parent='', index='end', iid='RED TEAM', text='',
                   values='-')
    my_game.place(anchor='nw', width=140, height=62, relx=0.3, rely=0.3)
    return my_game


def updateWinnerTeamTab(game_frame, winner):
    game_frame.delete('BLUE TEAM')
    game_frame.delete('RED TEAM')
    if winner == 1:
        winner = 'BLUE TEAM'
        loser = 'RED TEAM'
    else:
        winner = 'RED TEAM'
        loser = 'BLUE TEAM'
    game_frame.insert(parent='', index=0, iid=winner, text='', values=winner)
    game_frame.insert(parent='', index=1, iid=loser, text='', values=loser)



def updateTab(my_game, agent):
    my_game.delete(agent.id)
    if agent.isGonnaCharge:
        charge = "Va se charger"
    else:
        charge = "-"
    if agent.tacheToDo is None:
        my_game.insert(parent='', index=agent.id, iid=agent.id, text='',
                       values=(agent.id, str(int(agent.charge / agent.autonomie * 100)) + "%",
                               agent.trajet[agent.caseOfTrajet].getCoords(),
                               agent.score,
                               "No task", "No task", agent.wearing, charge))
    else:
        my_game.insert(parent='', index=agent.id, iid=agent.id, text='',
                       values=(agent.id, str(int(agent.charge / agent.autonomie * 100)) + "%",
                               agent.trajet[agent.caseOfTrajet].getCoords(),
                               agent.score,
                               agent.tacheToDo.depart.getType(),
                               agent.tacheToDo.arrivee.getType(),
                               agent.wearing, charge))
    return my_game


def getScore(my_game):
    children = my_game.get_children()
    score = 0
    for i in children:
        score += my_game.item(i)['values'][3]
    return score


def createScoreValue(frame, score):
    font = tkFont.Font(family='Verdana', size=18, weight='bold')
    label = tkinter.Label(
        frame, text=score, justify='left', font=font
    )
    label.place(anchor='nw', relx=0.8, rely=0.055)
    return label


def updateScoreValue(label, score):
    label.config(text=score)


def createTaskIcon(cv, dpt):
    exc = Image.open('img/Exclamation.png')
    im = ImageTk.PhotoImage(exc)
    c = cv.create_image(0, 0, image=im, anchor='nw')
    cv.tag_raise(c)
    cv.update()
    return c


def createImg(cv, coords, equipe):
    if equipe == 0:
        skin = cv.create_oval(coords[0] * 12, coords[1] * 12, (coords[0] + 1) * 12, (coords[1] + 1) * 12,
                              fill='blue')
    else:
        skin = cv.create_oval(coords[0] * 12, coords[1] * 12, (coords[0] + 1) * 12, (coords[1] + 1) * 12,
                              fill='red')

    # cv.create_rectangle(500, 500, 800, 800, fill='white')
    # cv.update()
    return skin


class Interface:
    def __init__(self, img):
        self.root = Tk()
        self.root.resizable(False, False)

        self.img = Image.open('img/' + img, 'r').convert('RGB')

    def getPx(self):
        """
        récupère un tableau de chaque pixel de l'image donnée en paramètre
        :return: liste de tous les pixels
        """
        return self.img.load()

    def createWindow(self):
        w_image, h_image = self.img.size
        self.root.geometry('860x' + str(h_image * 18 - 4))
        

    def createCanvas(self):
        w_image, h_image = self.img.size
        # self.root.geometry('860x' + str(h_image * 18-4))
        cv = Canvas(self.root, height=h_image * 12, width=w_image * 12)
        cv.grid(sticky="nw")

        # self.root.grid_columnconfigure(0, weight=1)
        # self.root.grid_columnconfigure(3, weight=1)
        # self.root.update_idletasks()
        cv.update()
        return cv

    @staticmethod
    def createLieu(cv, coordX, coordY, color):
        cv.create_rectangle(coordX, coordY, coordX + 12, coordY + 12, fill=color, width=1, outline='#0b181c')

    @staticmethod
    def createRoad(cv, coordX, coordY):
        cv.create_rectangle(coordX, coordY, coordX + 12, coordY + 12, fill='#efe4c6', width=1, outline='#967979')

    @staticmethod
    def createDecor(cv, coordX, coordY):
        cv.create_rectangle(coordX, coordY, coordX + 12, coordY + 12, fill='#000000', width=1)

    def main_loop(self):
        """
        Fonction tkinter qui garde la fenêtre active
        :return: void
        """
        self.root.mainloop()

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
        cv.move(id, coords[0] * 12, coords[1] * 12)

    def skins_map_update(self, cv: Canvas, mapS, skins):
        if mapS:
            cv.delete(mapS)
        im = Image.open('img/fond_route.png')
        imdec = Image.open('img/decor.png')
        h, w = self.img.size
        nim = im.resize((h * 12, w * 12), Image.ANTIALIAS)
        nimdec = imdec.resize((h * 12, w * 12), Image.ANTIALIAS)
        im = ImageTk.PhotoImage(nim)
        imdec = ImageTk.PhotoImage(nimdec)

        mapS = cv.create_image(0, 0, image=im, anchor=NW, disabledimage=im)

        if skins:
            for i in range(len(skins)):
                cv.tag_raise(skins[i])

        mapS = cv.create_image(0, 0, image=imdec, anchor=NW, disabledimage=imdec)

        # cv.create_rectangle(0, 0, h*20, w*20, fill='white')
        cv.update()
        return mapS

    def createIcon(self, icon):
        t = PhotoImage(file=icon)
        self.root.tk.call('wm', 'iconphoto', '.', t)

    def getWidth(self):
        return self.img.size

    def addFrame(self, row, column, w, h):
        if row == 0:
            game_frame = Frame(self.root, width=w, height=h)
            game_frame.place(relx=0.67)
        else:
            game_frame = Frame(self.root, width=w, height=h)
            game_frame.grid(row=row, column=column)

        return game_frame

    def gameFini(self, team):
        font = tkFont.Font(family='Verdana', size=36, weight='bold')
        if team == 0:
            team = 'RED'
        else:
            team = 'BLUE'
        frame = Frame(self.root, width=960, height=960)
        frame.grid(row=0, column=1, sticky='N')
        label = tkinter.Label(
            frame, text=team + ' TEAM WIN', font=font, justify='center'
        )
        label.place(anchor='n', relx=0.5, rely=0.3)
