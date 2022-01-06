from src.Interface import *


class SimMenu:
    def __init__(self):
        self.itf = Interface('menu.png')
        self.team = []

        self.heuristiqueE1 = 0
        self.heuristiqueE2 = 0

        self.nbAgentE1 = 2
        self.nbAgentE2 = 2

        self.nbTaches = 30

        self.choixTacheE1 = 0
        self.choixTacheE2 = 0

        self.bienvenue()
        self.chooseAgentE1()
        self.chooseAgentE2()
        self.chooseTaches()
        self.chooseHeuristiqueE1()
        self.chooseHeuristiqueE2()
        self.chooseChoixTachesE1()
        self.chooseChoixTachesE2()
        self.destroy()

    def start(self):
        self.itf.createWindow()
        self.itf.main_loop()

    # Label bienvenue
    def bienvenue(self):
        font = tkFont.Font(family='Verdana', size=18, weight='bold')
        label = tkinter.Label(
            self.itf.root, text="Bienvenue dans le projet SMART CITY de la SMART CORP"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.05, rely=0.05)

    ########################################
    # Choix des agents pour les deux equipes
    ########################################
    def chooseAgentE1(self):
        font = tkFont.Font(family='Verdana', size=18, weight='bold')
        label = tkinter.Label(
            self.itf.root, text="Choisissez le nombre d'agents"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.25, rely=0.2)
        label = tkinter.Label(
            self.itf.root, text="Equipe 1"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.2, rely=0.25)

        addButton(self.itf.root, 0.3, 0.17, '1', lambda: self.commandButtonTeam1(1))
        addButton(self.itf.root, 0.3, 0.22, '2', lambda: self.commandButtonTeam1(2))
        addButton(self.itf.root, 0.3, 0.27, '3', lambda: self.commandButtonTeam1(3))
        addButton(self.itf.root, 0.3, 0.32, '4', lambda: self.commandButtonTeam1(4))

    def chooseAgentE2(self):
        font = tkFont.Font(family='Verdana', size=18, weight='bold')
        label = tkinter.Label(
            self.itf.root, text="Equipe 2"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.6, rely=0.25)

        addButton(self.itf.root, 0.3, 0.57, '1', lambda: self.commandButtonTeam2(1))
        addButton(self.itf.root, 0.3, 0.62, '2', lambda: self.commandButtonTeam2(2))
        addButton(self.itf.root, 0.3, 0.67, '3', lambda: self.commandButtonTeam2(3))
        addButton(self.itf.root, 0.3, 0.72, '4', lambda: self.commandButtonTeam2(4))

    def commandButtonTeam1(self, button):
        self.nbAgentE1 = button

    def commandButtonTeam2(self, button):
        self.nbAgentE2 = button

    ###########################
    # Choix du nombre de taches
    ###########################

    def chooseTaches(self):
        font = tkFont.Font(family='Verdana', size=18, weight='bold')
        label = tkinter.Label(
            self.itf.root, text="Choisissez le nombre de taches"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.25, rely=0.4)
        label = tkinter.Label(
            self.itf.root, text="Equipe 1"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.2, rely=0.25)

        addButton(self.itf.root, 0.45, 0.27, '10', lambda: self.commandButtonTaches(10))
        addButton(self.itf.root, 0.45, 0.37, '20', lambda: self.commandButtonTaches(20))
        addButton(self.itf.root, 0.45, 0.47, '30', lambda: self.commandButtonTaches(30))
        addButton(self.itf.root, 0.45, 0.57, '40', lambda: self.commandButtonTaches(40))
        addButton(self.itf.root, 0.45, 0.67, '50', lambda: self.commandButtonTaches(50))

    def commandButtonTaches(self, button):
        self.nbTaches = button

    ##################################
    # Choix du deplacement des equipes
    ##################################

    def chooseHeuristiqueE1(self):
        font = tkFont.Font(family='Verdana', size=18, weight='bold')
        label = tkinter.Label(
            self.itf.root, text="Choisissez l'heuristique des equipes"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.20, rely=0.53)
        label = tkinter.Label(
            self.itf.root, text="Equipe 1"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.2, rely=0.6)

        addButton(self.itf.root, 0.66, 0.11, 'Manhattan', lambda: self.commandButtonHE1(0))
        addButton(self.itf.root, 0.66, 0.225, 'Pythagore', lambda: self.commandButtonHE1(1))
        addButton(self.itf.root, 0.66, 0.335, 'Dijkstra', lambda: self.commandButtonHE1(2))

    def chooseHeuristiqueE2(self):
        font = tkFont.Font(family='Verdana', size=18, weight='bold')
        label = tkinter.Label(
            self.itf.root, text="Equipe 2"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.6, rely=0.6)

        addButton(self.itf.root, 0.66, 0.52, 'Manhattan', lambda: self.commandButtonHE2(0))
        addButton(self.itf.root, 0.66, 0.64, 'Pythagore', lambda: self.commandButtonHE2(1))
        addButton(self.itf.root, 0.66, 0.755, 'Dijkstra', lambda: self.commandButtonHE2(2))

    def commandButtonHE1(self, button):
        self.heuristiqueE1 = button

    def commandButtonHE2(self, button):
        self.heuristiqueE2 = button

    ###########################
    # Choix du choix des taches
    ###########################
    def chooseChoixTachesE1(self):
        font = tkFont.Font(family='Verdana', size=18, weight='bold')
        label = tkinter.Label(
            self.itf.root, text="Choisissez le choix des taches des equipes"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.17, rely=0.75)
        label = tkinter.Label(
            self.itf.root, text="Equipe 1"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.2, rely=0.8)

        addButton(self.itf.root, 0.86, 0.11, 'Aléatoire', lambda: self.commandChoixTacheE1(0))
        addButton(self.itf.root, 0.86, 0.21, 'Rentable', lambda: self.commandChoixTacheE1(1))
        addButton(self.itf.root, 0.86, 0.31, 'Proximité', lambda: self.commandChoixTacheE1(2))

    def chooseChoixTachesE2(self):
        font = tkFont.Font(family='Verdana', size=18, weight='bold')
        label = tkinter.Label(
            self.itf.root, text="Equipe 2"
            , font=font, justify='center'
        )
        label.place(anchor='nw', relx=0.6, rely=0.8)

        addButton(self.itf.root, 0.86, 0.53, 'Aléatoire', lambda: self.commandChoixTacheE2(0))
        addButton(self.itf.root, 0.86, 0.63, 'Rentable', lambda: self.commandChoixTacheE2(1))
        addButton(self.itf.root, 0.86, 0.73, 'Proximité', lambda: self.commandChoixTacheE2(2))

    def commandChoixTacheE1(self, button):
        self.choixTacheE1 = button

    def commandChoixTacheE2(self, button):
        self.choixTacheE2 = button

    def destroy(self):
        w = tkinter.Button(self.itf.root, text='Start', command = lambda : self.itf.root.destroy(),
                           height = 3, width = 5)
        w.place(anchor="nw", rely=0.9, relx=0.43)
        return w

