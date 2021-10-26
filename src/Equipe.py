import Agent

class equipe:

    def __init__(self, id: int, nom: str, agents: list):
        self.id = id
        self.nom = nom
        self.agents = agents

    
    def getAgents(self) -> list:
        return self.agents