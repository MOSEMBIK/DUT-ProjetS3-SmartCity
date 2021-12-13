from src.Interface import *


class Layer:
    def __init__(self, interface, equipe):
        self.itf: Interface = interface

        # Creation des frames
        self.frame1 = self.itf.addFrame(0)
        self.frame2 = self.itf.addFrame(2)

        # Creation des tableaux
        self.tab1 = addBoard(self.frame1, equipe[0].getAgents())
        self.tab2 = addBoard(self.frame2, equipe[1].getAgents())


        # Score equipe 1 et 2
        self.score1 = 0
        self.score2 = 0

        # Label score 1 et 2 touchez pas c dla merde mais osef

        self.label1 = createScoreValue(self.frame1, self.score1)

        # Ajout widgets
        addText("Score", self.frame1)
        addText("Score", self.frame2)

    def updateScore(self):
        self.score1 = getScore(self.tab1)
        updateScoreValue(self.label1, self.score1)

    def updateCharge(self, charge):
        self.score1 = charge
        # addScore(self.score1, self.frame1)

    def updateTab(self, agent):
        if int(agent.id) < 10:
            self.tab1 = updateTab(self.tab1, agent)
        else:
            self.tab2 = updateTab(self.tab2, agent)
        # updateTab(self.tab2, agent)
