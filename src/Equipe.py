from src.Agent import *
from src.Plateau import *
from src.Case import *

class Equipe:

    def __init__(self, id: int, nom: str = ""):
        self.id = id
        self.nom = nom
        self.agents = {}
    
    def getAgents(self) -> dict:
        return self.agents
    
    def addAgents(self, id : int, type : int = 0) -> None:
        self.agents[id] = Agent(id, type)
        return None
    
    # Déplacement
    def agentMoveSimple(self, id : int) -> None:
        self.agents.get(id).moveSimple()
        return None
    
    def agentMove(self, id : int, plt : Plateau) -> None:
        self.agents.get(id).move(plt)
        return None
    
    # Destination
    def agentGoToRandom(self, id : int, plt : Plateau) -> None:
        self.agents.get(id).goToRandom(plt)
        return None
    
    def agentGoTo(self, id : int, plt : Plateau, case : Case) -> None:
        """
        Requete qui parametre le déplacement d'un Agent vers une case.

        :param id: Identifiant de l'Agent sur lequel porte la requete
        :param plt: Plateau sur lequel l'Agent se situe
        :param case: Case de destination
        """
        self.agents.get(id).goTo(plt, case)
        return None