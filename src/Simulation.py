from src.Equipe import *
from src.Agent import *
from src.Plateau import *
from src.Case import *
from src.Layer import *
import random as rdm


class Simulation:

    def __init__(self, name: str = "", ico : str = None, nbAgentE1: int = 2, nbAgentE2: int = 2, nbTaches = 50, nbTachesSim = 10):
        self.name = name
        self.itf = Interface('Squelette_map.png')
        self.plt: Plateau = Plateau(self.name, ico, self.itf)
        self.skin = {}
        self.equipe: list[Equipe] = []
        self.taches: list[Tache] = []
        self.createTaches(nbTaches)
        for i in range(nbTachesSim):
            t = rdm.choice(self.taches)
            self.plt.listeTaches.append(t)
            self.taches.pop(self.taches.index(t))
        for i in range(1):
            self.equipe.append(Equipe(i))
            if i == 0:
                for j in range(nbAgentE1):
                    idAgent = str(i) + str(j)
                    self.equipe[i].addAgents(idAgent, self.plt.getLieu('Spawn')[0])
                    self.skin[self.equipe[i].getAgents()[idAgent]] = createImg(self.plt.canvas, self.equipe[i].getAgents()[idAgent].spawn.getCoords(), i)
            if i == 1:
                for j in range(nbAgentE2):
                    idAgent = str(i) + str(j)
                    self.equipe[i].addAgents(idAgent, self.plt.getLieu('Spawn')[0])
                    self.skin[self.equipe[i].getAgents()[idAgent]] = createImg(self.plt.canvas, self.equipe[i].getAgents()[idAgent].spawn.getCoords(), i)

        self.layer: Layer = Layer(self.itf, self.equipe)

    # Déplacement
    def agentMoveSimple(self, idE: int, idA: str) -> None:
        self.equipe[idE].agentMoveSimple(idA)
        return None

    def agentMove(self, idE: int, idA: str) -> None:
        self.equipe[idE].agentMove(idA, self.plt)
        return None

    def allMove(self, mode: int = 0) -> None:
        # Mode complexe (gestion charge, vitesse, ...)
        if mode == 0:
            for idE in range(len(self.equipe)):
                for idA in self.equipe[idE].getAgents():
                    self.agentMove(idE, idA)
        # Mode simple
        else:
            for idE in range(len(self.equipe)):
                for idA in self.equipe[idE].getAgents():
                    self.agentMoveSimple(idE, idA)
        return None

    # Destination
    def agentGoToRandom(self, idE: int, idA: str, ) -> None:
        self.equipe[idE].agentGoToRandom(idA, self.plt)
        return None

    def allGoToRandom(self) -> None:
        for idE in range(len(self.equipe)):
            for idA in self.equipe[idE].getAgents():
                self.agentGoToRandom(idE, idA)
        return None

    def agentGoTo(self, idE: int, idA: str, case: Case) -> None:
        self.equipe[idE].agentGoTo(idA, self.plt, case)
        return None

    def createTaches(self, nbTaches):
        for i in range(nbTaches):
            portes2 = self.plt.getPortes()
            dpt = rdm.choice(portes2)
            portes2.pop(portes2.index(dpt))
            arv = rdm.choice(portes2)
            volume = randint(10,100)
            tache = Tache(dpt, arv, volume, self.plt)
            # createTaskIcon(self.canvas, dpt)
            self.taches.append(tache)
        return None