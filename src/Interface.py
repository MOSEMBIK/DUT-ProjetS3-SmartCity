import tkinter
import tkinter.ttk
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont

from src.Agent import *


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


def addButton(frame, x, y, text, callback):
    w = tkinter.Button(frame, text=text, command=callback)
    w.place(anchor="nw", rely=x, relx=y)
    return w


def addBoard(game_frame, agents):
    style = tkinter.ttk.Style()
    style.configure("Treeview", font=('Calibri', 11))

    my_game = tkinter.ttk.Treeview(game_frame, style="Treeview")
    my_game['columns'] = ('agent_id', 'autonomie', 'position', 'score', 'Départ', 'Arrivée', 'volume', 'Va charger')

    my_game.column("#0", width=0, stretch=NO)
    my_game.column("agent_id", anchor=CENTER, width=20)
    my_game.column("autonomie", anchor=CENTER, width=60)
    my_game.column("position", anchor=CENTER, width=60)
    my_game.column("score", anchor=CENTER, width=60)
    my_game.column("Départ", anchor=CENTER, width=130)
    my_game.column("Arrivée", anchor=CENTER, width=130)
    my_game.column("volume", anchor=CENTER, width=40)
    my_game.column("Va charger", anchor=CENTER, width=60)

    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("agent_id", text="ID", anchor=CENTER)
    my_game.heading("autonomie", text="Charge", anchor=CENTER)
    my_game.heading("position", text="Position", anchor=CENTER)
    my_game.heading("score", text="Score", anchor=CENTER)
    my_game.heading("Départ", text="Départ", anchor=CENTER)
    my_game.heading("Arrivée", text="Arrivée", anchor=CENTER)
    my_game.heading("volume", text="Volume", anchor=CENTER)
    my_game.heading("Va charger", text="Va charger", anchor=CENTER)

    for i in agents.keys():
        agent: Agent = agents[i]

        my_game.insert(parent='', index='end', iid=agent.id, text='',
                       values=(agent.id,
                               agent.charge / agent.autonomie * 100,
                               0,
                               agent.score,
                               "-",
                               "-",
                               0, '-'))

    my_game.place(anchor='nw', width=860, height=140, rely=0.3)
    return my_game

    # def updateBoard(selfself, column):


def createWinnerTeamTab(game_frame):
    font = tkFont.Font(family='Verdana', size=12, weight='bold')
    label = tkinter.Label(
        game_frame, text="Equipe gagnante :"
        , font=font, justify='center'
    )
    label.place(anchor='nw', relx=0.23, rely=0.30)

    style = tkinter.ttk.Style()
    style.configure("Treeview.Heading", font=(None, 9))

    style.configure("Treeview", font=('Calibri', 9))

    my_game = tkinter.ttk.Treeview(game_frame, style="Treeview")
    my_game['columns'] = ('Equipe', 'heuristique', 'choixTache')

    my_game.column("#0", width=0, stretch=NO)
    my_game.column("Equipe", anchor=CENTER, width=40)
    my_game.column("heuristique", anchor=CENTER, width=40)
    my_game.column("choixTache", anchor=CENTER, width=40)

    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("Equipe", text="Equipe W", anchor=CENTER)
    my_game.heading("heuristique", text="Heuristique", anchor=CENTER)
    my_game.heading("choixTache", text="choixTache", anchor=CENTER)

    my_game.insert(parent='', index='end', iid='BLUE TEAM', text='',
                   values=('-', '-', '-'))

    my_game.insert(parent='', index='end', iid='RED TEAM', text='',
                   values=('-', '-', '-'))
    my_game.place(anchor='nw', width=300, height=62, relx=0, rely=0.35)
    return my_game


def updateWinnerTeamTab(game_frame, winner, equipe):
    game_frame.delete('BLUE TEAM')
    game_frame.delete('RED TEAM')

    if winner == 1:
        equipeW = equipe[0]
        equipeL = equipe[1]
        winner = 'BLUE TEAM'
        loser = 'RED TEAM'
    else:
        equipeW = equipe[1]
        equipeL = equipe[0]
        winner = 'RED TEAM'
        loser = 'BLUE TEAM'
    equipeWHeuristique = getStrHeuristique(list(equipeW.getAgents().values())[0].heuristique)
    equipeWChoixT = getStrChoixT(list(equipeW.getAgents().values())[0].choixT)
    equipeLHeuristique = getStrHeuristique(list(equipeL.getAgents().values())[0].heuristique)
    equipeLChoixT = getStrChoixT(list(equipeL.getAgents().values())[0].choixT)

    game_frame.insert(parent='', index=0, iid=winner, text='',
                      values=(winner,
                              equipeWHeuristique,
                              equipeWChoixT))
    game_frame.insert(parent='', index=1, iid=loser, text='',
                      values=(loser, equipeLHeuristique,
                              equipeLChoixT))


def updateTab(my_game, agent):
    my_game.delete(agent.id)
    if agent.isGonnaCharge:
        charge = "X"
    else:
        charge = "-"
    if agent.tacheToDo is None:
        if agent.tacheChose is None:
            my_game.insert(parent='', index=agent.id, iid=agent.id, text='',
                           values=(agent.id, str(int(agent.charge / agent.autonomie * 100)) + "%",
                                   str(int(agent.trajet[agent.caseOfTrajet].getCoords()[0])) + " " + str(
                                       int(agent.trajet[agent.caseOfTrajet].getCoords()[1])),
                                   agent.score,
                                   "-", "-", agent.wearing, charge))
        else:
            my_game.insert(parent='', index=agent.id, iid=agent.id, text='',
                           values=(agent.id, str(int(agent.charge / agent.autonomie * 100)) + "%",
                                   str(int(agent.trajet[agent.caseOfTrajet].getCoords()[0])) + " " + str(
                                       int(agent.trajet[agent.caseOfTrajet].getCoords()[1])),
                                   agent.score,
                                   agent.tacheChose.depart.getType(), "-", agent.wearing, charge))
    else:
        my_game.insert(parent='', index=agent.id, iid=agent.id, text='',
                       values=(agent.id, str(int(agent.charge / agent.autonomie * 100)) + "%",
                               str(int(agent.trajet[agent.caseOfTrajet].getCoords()[0])) + " " + str(
                                   int(agent.trajet[agent.caseOfTrajet].getCoords()[1])),
                               agent.score,
                               agent.tacheToDo.depart.getType(),
                               agent.tacheToDo.arrivee.getType(),
                               agent.wearing, charge))
    return my_game


def getStrHeuristique(heuristique):
    if heuristique == 0:
        return "Mannhattan"
    elif heuristique == 1:
        return "Pythagore"
    elif heuristique == 2:
        return "Dijsktra"


def getStrChoixT(choix):
    if choix == 0:
        return "Aleatoire"
    elif choix == 1:
        return "Rentable"
    else:
        return "Proximité"


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


def addSmartCorp(frame):
    font = tkFont.Font(family='Verdana', size=16, weight='bold')
    label = tkinter.Label(
        frame, text="Simulation Smart Corp"
        , font=font, justify='center'
    )
    label.place(anchor='nw', relx=0.01, rely=0.05)


def showTaches(frame, taches, tachesDispo):
    ######################
    ######## H1 ##########
    ######################
    font = tkFont.Font(family='Verdana', size=12)
    label = tkinter.Label(
        frame, text="Nombre de taches :"
        , font=font, justify='center'
    )
    label.place(anchor='nw', relx=0.03, rely=0.2)

    label = tkinter.Label(
        frame, text="Nombre de taches dispos :"
        , font=font, justify='center'
    )
    label.place(anchor='nw', relx=0.03, rely=0.25)

    font = tkFont.Font(family='Verdana', size=10)
    label = tkinter.Label(
        frame, text="/ " + str(taches), justify='center', font=font
    )
    label.place(anchor='nw', relx=0.62, rely=0.205)

    font = tkFont.Font(family='Verdana', size=10)
    label = tkinter.Label(
        frame, text="/ " + str(tachesDispo), justify='center', font=font
    )
    label.place(anchor='nw', relx=0.77, rely=0.255)

    # Taches choisises


def createTacheValue(frame, taches):
    font = tkFont.Font(family='Verdana', size=10)
    label = tkinter.Label(
        frame, text=taches, justify='center', font=font
    )
    label.place(anchor='nw', relx=0.55, rely=0.205)
    return label


def createTacheDispoValue(frame, taches):
    font = tkFont.Font(family='Verdana', size=10)
    label = tkinter.Label(
        frame, text=taches, justify='center', font=font
    )
    label.place(anchor='nw', relx=0.71, rely=0.255)
    return label


def createLeaderBoard(game_frame, agents0, agents1):
    font = tkFont.Font(family='Verdana', size=12, weight='bold')
    label = tkinter.Label(
        game_frame, text="Classement :"
        , font=font, justify='center'
    )
    label.place(anchor='nw', relx=0.29, rely=0.47)

    style = tkinter.ttk.Style()
    style.configure("Treeview.Heading", font=(None, 9))

    style.configure("Treeview", font=('Calibri', 9))

    my_game = tkinter.ttk.Treeview(game_frame, style="Treeview")
    my_game['columns'] = ('id', 'equipe', 'score')

    my_game.column("#0", width=0, stretch=NO)
    my_game.column("id", anchor=CENTER, width=40)
    my_game.column("equipe", anchor=CENTER, width=40)
    my_game.column("score", anchor=CENTER, width=40)

    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("id", text="ID", anchor=CENTER)
    my_game.heading("equipe", text="Equipe", anchor=CENTER)
    my_game.heading("score", text="Points", anchor=CENTER)

    for i in agents0.keys():
        agent: Agent = agents0[i]

        my_game.insert(parent='', index='end', iid=agent.id, text='',
                       values=(agent.id, 'blue', agent.score))
    for i in agents1.keys():
        agent: Agent = agents1[i]

        my_game.insert(parent='', index='end', iid=agent.id, text='',
                       values=(agent.id, 'red', agent.score))
    my_game.place(anchor='nw', width=300, height=180, rely=0.52)
    return my_game


def updateLeaderBoard(my_game, agent):
    my_game.delete(agent.id)
    lstId = list(agent.id)
    children = my_game.get_children()
    scoreAgent = []
    for i in children:
        scoreAgent.append(my_game.item(i)['values'][2])
    scoreAgent = sorted(scoreAgent, reverse=True)
    index = len(scoreAgent)+1
    for i in range(len(scoreAgent)):
        if agent.score > scoreAgent[i]:
            index = i
            break

    if lstId[0] == '0':
        team = 'BLUE'
    else:
        team = 'RED'
    my_game.insert(parent='', index=index, iid=agent.id, text='',
                   values=(agent.id, team, agent.score))
    return my_game


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
        self.root.geometry('860x860')

    def createCanvas(self):
        w_image, h_image = self.img.size
        cv = Canvas(self.root, height=h_image * 12, width=w_image * 12)
        cv.grid(sticky="nw")
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
        if team == 1:
            team = 'RED'
        else:
            team = 'BLUE'
        frame = Frame(self.root, width=960, height=960)
        frame.grid(row=0, column=1, sticky='N')
        label = tkinter.Label(
            frame, text=team + ' TEAM WIN', font=font, justify='center'
        )
        label.grid(row = 0, column = 0)
