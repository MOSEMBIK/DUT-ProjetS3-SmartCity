from src.Agent import *
from src.Plateau import *
from src.Case import *

class Equipe:

    def __init__(self, id: int, nom: str = ""):
        self.id = id
        self.nom = nom
        self.agents : dict[str,Agent] = {}
    
    def getAgents(self) -> dict[str,Agent]:
        return self.agents
    
    def addAgents(self, id : str, spawn : Case) -> None:
        self.agents[id] = Agent(id, spawn)
        return None
    
    # Déplacement
    def agentMoveSimple(self, id : str) -> None:
        self.agents.get(id).moveSimple()
        return None
    
    def agentMove(self, id : str, plt : Plateau) -> None:
        self.agents.get(id).move2(plt)
        return None
    
    # Destination
    def agentGoToRandom(self, id : str, plt : Plateau) -> None:
        self.agents.get(id).goToRandom(plt)
        return None
    
    def agentGoTo(self, id : str, plt : Plateau, case : Case) -> None:
        """
        Requete qui parametre le déplacement d'un Agent vers une case.

        :param id: Identifiant de l'Agent sur lequel porte la requete
        :param plt: Plateau sur lequel l'Agent se situe
        :param case: Case de destination
        """
        self.agents.get(id).goTo(plt, case)
        return None