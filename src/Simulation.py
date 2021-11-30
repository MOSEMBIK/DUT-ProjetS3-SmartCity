from src.Equipe import *
from src.Agent import *
from src.Plateau import *
from src.Case import *


class Simulation:

    def __init__(self, name: str = "", ico : str = None, nbEquipe: int = 1, nameEquipe: str = "", nbAgent: int = 1):
        self.name = name
        self.plt: Plateau = Plateau(self.name, ico)
        self.skin = {}
        self.equipe: list[Equipe] = []
        for i in range(nbEquipe):
            self.equipe.append(Equipe(i, nameEquipe))
            for j in range(nbAgent):
                idAgent = str(i) + str(j)
                self.equipe[i].addAgents(int(idAgent), self.plt.edges)
                self.skin[self.equipe[i].getAgents()[int(idAgent)]] = self.plt.itf.createImg(self.plt.canvas, self.equipe[i].getAgents()[int(idAgent)].spawn)
                #self.skin[self.equipe[i].getAgents()[int(idAgent)]] = self.plt.itf.setSkin(self.equipe[i].getAgents()[int(idAgent)].spawn, 'war.png')

    # Déplacement
    def agentMoveSimple(self, idE: int, idA: int) -> None:
        self.equipe[idE].agentMoveSimple(idA)
        return None

    def agentMove(self, idE: int, idA: int) -> None:
        self.equipe[idE].agentMove(idA, self.plt)
        return None

    def allMove(self, mode: int = 0) -> None:
        # Mode complexe (gestion charge, vitesse, ...)
        if mode == 0:
            for idE in range(len(self.equipe)):
                for idA in range(len(self.equipe[idE].getAgents())):
                    self.agentMove(idE, idA)
        # Mode simple
        else:
            for idE in range(len(self.equipe)):
                for idA in range(len(self.equipe[idE].getAgents())):
                    self.agentMoveSimple(idE, idA)
        return None

    # Destination
    def agentGoToRandom(self, idE: int, idA: int, ) -> None:
        self.equipe[idE].agentGoToRandom(idA, self.plt)
        return None

    def allGoToRandom(self) -> None:
        for idE in range(len(self.equipe)):
            for idA in range(len(self.equipe[idE].getAgents())):
                self.agentGoToRandom(idE, idA)
        return None

    def agentGoTo(self, idE: int, idA: int, case: Case) -> None:
        self.equipe[idE].agentGoTo(idA, self.plt, case)
        return None
