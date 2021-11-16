from src.Agent import *
from src.Environnement import *
from src.Case import *

class Equipe:

    def __init__(self, id: int, nom: str = ""):
        self.id = id
        self.nom = nom
        self.agents = {}
    
    def getAgents(self) -> list:
        return self.agents
    
    def addAgents(self, id : int, type : int = 0) -> None:
        self.agents[id] = Agent(id, type)
        return None
    
    def moveAgent(self, id : int) -> None:

        return None