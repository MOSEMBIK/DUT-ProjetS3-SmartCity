from src.Agent import *
from src.Plateau import *
from src.Case import *

class Equipe:

    def __init__(self, id: int, nom: str = ""):
        self.id = id
        self.nom = nom
        self.agents = {int:Agent}
    
    def getAgents(self) -> dict:
        return self.agents
    
    def addAgents(self, id : int, type : int = 0) -> None:
        self.agents[id] = Agent(id, type)
        return None
    
    def agentMove(self, id : int, plt : Plateau) -> None:
        self.agents.get(id).move(plt)
        return None
    
    def agentGoTo(self, id : int) -> None:

        return None