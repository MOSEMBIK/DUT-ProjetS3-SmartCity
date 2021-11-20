from src.Equipe import *
from src.Agent import *
from src.Plateau import *
from src.Case import *

class Simulation :

    def __init__(self, name: str, nbEquipe : int = 1, nameEquipe : int = None, nbAgent : int = 1, typeAgent : int = None, envName : str = None):
        self.name = name

        self.equipe = [Equipe]
        for i in range(nbEquipe):
            self.equipe.append(Equipe(i, nameEquipe))
            for j in range(nbAgent) :
                self.equipe[i].addAgents(j, typeAgent)

        self.env = Plateau(envName)
    

    
    # Déplacement
    def agentMoveSimple(self, idE : int, idA : int) -> None:
        self.equipe[idE].agentMoveSimple(idA)
        return None

    def agentMove(self, idE : int, idA : int) -> None:
        self.equipe[idE].agentMove(idA, self.env)
        return None
    
    def allMove(self, mode : int = 0) -> None:
        # Mode complexe (gestion charge, vitesse, ...)
        if mode == 0:
            for idE in range(len(self.equipe)) :
                for idA in range(len(self.equipe[idE].getAgents())) :
                    self.agentMove(idE, idA)
        # Mode simple
        else : 
            for idE in range(len(self.equipe)) :
                for idA in range(len(self.equipe[idE].getAgents())) :
                    self.agentMoveSimple(idE, idA)
        return None
    


    # Destination
    def agentGoToRandom(self, idE : int, idA : int,) -> None:
        self.equipe[idE].agentGoToRandom(idA, self.env)
        return None
    
    def allGoToRandom(self) -> None:
        for idE in range(len(self.equipe)) :
            for idA in range(len(self.equipe[idE].getAgents())) :
                self.agentGoToRandom(idE, idA)
        return None
    

    def agentGoTo(self, idE : int, idA : int, case : Case) -> None:
        self.equipe[idE].agentGoTo(idA, self.env, case)
        return None
    
    def allGoTo(self) -> None:

        return None
