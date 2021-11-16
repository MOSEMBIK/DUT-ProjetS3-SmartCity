from src.Equipe import *
from src.Agent import *
from src.Environnement import *
from src.Case import *

class Interface:

    def __init__(self, name: str, nbEquipe : int = 1, nameEquipe : int = None, nbAgent : int = 1, typeAgent : int = None, envName : str = None):
        self.name = name

        self.equipe = [Equipe]
        for i in range(nbEquipe):
            self.equipe.append(Equipe(i, nameEquipe))
            for j in range(nbAgent) :
                self.equipe[i].addAgents(j, typeAgent)

        self.env = Environnement(envName)
