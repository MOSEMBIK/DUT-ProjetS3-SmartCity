import asyncio

from src.Case import *

class Agent:

    def __init__(self, id: int, type: int) -> None:
        self.id = id

        # Test de la validité du type
        try :
            if (self.type in (0, 2)) :
                self.type = type
        except :
            raise Exception("Invalid Agent.type parameter given.")

        self.location = None

        # Parametrage de la vitesse selon le type
        if (self.type == 0) :
            self.speed = 1.5
        elif (self.type == 1) :
            self.speed = 0.75
        elif (self.type == 2) :
            self.speed = 0.50
        
        # Parametrage de l'autonomie selon le type
        if (self.type == 0) :
            self.autonomie = 1500
        elif (self.type == 1) :
            self.autonomie = 900
        elif (self.type == 2) :
            self.autonomie = 8000
        
        # Parametrage du volumeMax selon le type
        if (self.type == 0) :
            self.volumeMax = 15
        elif (self.type == 1) :
            self.volumeMax = 55
        elif (self.type == 2) :
            self.volumeMax = 150

        self.tache = None

    def initTrajet(self, destination: Case) -> list:
        Trajet = []
        # To do

        return Trajet

    async def move(self, trajet: list) -> None:
        while (self.location != trajet[-1].getCoord) :
            if ():
                return None