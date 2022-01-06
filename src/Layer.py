from src.Interface import *


class Layer:
    def __init__(self, interface, equipe):
        self.itf: Interface = interface
        self.equipe = equipe
        # Creation des frames
        self.frame1 = self.itf.addFrame(1, 0, 860, 140)
        self.frame2 = self.itf.addFrame(2, 0, 860, 140)
        self.frame3 = self.itf.addFrame(0, 0, 320, 580)

        # Creation des tableaux
        self.tab1 = addBoard(self.frame1, equipe[0].getAgents())
        self.tab2 = addBoard(self.frame2, equipe[1].getAgents())

        # Score equipe 1 et 2
        self.score1 = 0
        self.score2 = 0

        # Label score 1 et 2 touchez pas c dla merde mais osef

        self.label1 = createScoreValue(self.frame1, self.score1)
        self.label2 = createScoreValue(self.frame2, self.score2)

        self.accelerate = addButton(self.frame3, 0.8, 0.5, '>>', lambda: print('pause'))
        self.pause = addButton(self.frame3, 0.8, 0.4, "II", lambda: print("acceleration"))

        # Ajout widgets
        addText('BLUE', self.frame1)
        addText('RED', self.frame2)
        addSmartCorp(self.frame3)
        self.winnerTab = createWinnerTeamTab(self.frame3)

    def updateScore(self):
        self.score1 = getScore(self.tab1)
        self.score2 = getScore(self.tab2)
        updateScoreValue(self.label1, self.score1)
        updateScoreValue(self.label2, self.score2)
        updateWinnerTeamTab(self.winnerTab, self.getWinner(), self.equipe)

    def updateTab(self, agent):
        if int(agent.id) < 10:
            self.tab1 = updateTab(self.tab1, agent)
        else:
            self.tab2 = updateTab(self.tab2, agent)

    def getWinner(self):
        if self.score1 > self.score2:
            return 1
        return 2

    #def nbTaches(self, disp, ):
