from src.Environnement import *
from src.Case import *
from math import *
from src.Agent import *

class equipe:

    def __init__(self, id: int, nom: str, agents: list):
        self.id = id
        self.nom = nom
        self.agents = [Agent]
    
    def getAgents(self) -> list:
        return self.agents
    
    def addAgents(self, id : int, type : int = 0, n : int = 1) -> None:
        for i in range(n) :
            self.agents.append(Agent(id, type))
        return None