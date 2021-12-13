from src.Interface import *


class Layer:
    def __init__(self, interface, equipe):
        self.itf: Interface = interface

        # Creation des frames
        self.frame1 = self.itf.addFrame(0)
        self.frame2 = self.itf.addFrame(2)

        # Creation des tableaux
        self.tab1 = addBoard(self.frame1, equipe[0].getAgents())
        #self.tab2 = addBoard(self.frame2)

        # Equipes

        # Ajout widgets
        addText("Score", self.frame1)
        addText("Score", self.frame2)
        self.score1 = 0

    def updateCharge(self, charge):
        self.score1 = charge
        print(self.score1)
        # addScore(self.score1, self.frame1)

    def updateTab(self):
        updateTab(self.tab1, self.score1)
