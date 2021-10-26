from _typeshed import NoneType
from src.Environnement import *
from math import *

class Agent:

    def __init__(self, id: int, type: int):
        self.id = id
        # Test de la validité du type
        try :
            if (self.type in (0, 2)) :
                self.type = type
        except :
            raise Exception("Invalid Agent.type parameter given.")

        self.visibility = True

        # Parametrage de la vitesse selon le type
        if (self.type == 0) :
            self.speed = 4
        elif (self.type == 1) :
            self.speed = 2
        elif (self.type == 2) :
            self.speed = 1
        # Parametrage de l'autonomie selon le type
        if (self.type == 0) :
            self.autonomie = 2500
        elif (self.type == 1) :
            self.autonomie = 5000
        elif (self.type == 2) :
            self.autonomie = 8000
        # Parametrage du volumeMax selon le type
        if (self.type == 0) :
            self.volumeMax = 15
        elif (self.type == 1) :
            self.volumeMax = 55
        elif (self.type == 2) :
            self.volumeMax = 150

        self.caseOfTrajet = 0
        self.trajet = []

        self.score = 0


    def initTrajet(self, environnement: Environnement, positionL: Lieu, position: int, destinationL: Lieu, destination: int) -> None:
        size = environnement.getDimensions()
        lieux = environnement.getLieux()
        
        # Calcul vecteur Position->Destination
        def calcVec(p1 ,p2):
            dist = sqrt( (p1.getCoordonnes[0] - p2.getCoordonnes[0])**2 + (p1.getCoordonnes[1] - p2.getCoordonnes[1])**2 )
            return dist

        vec = calcVec(destinationL.getPattern()[destination], positionL.getPattern()[position])

        if destinationL.getPattern()[destination] and positionL.getPattern()[position] :
            for i in range(4):
                # En reflexion
                i = 0

        else :
            raise Exception ("Error")
        return None

    def move(self) -> Case:
        if self.caseOfTrajet + 1 < len(self.trajet):
            nextCase = self.trajet[self.caseOfTrajet + 1]
            self.caseOfTrajet += 1
        elif self.caseOfTrajet + 1 >= len(self.trajet):
            self.caseOfTrajet = 0
            self.trajet = [self.caseOfTrajet]
            nextCase = self.trajet[self.caseOfTrajet]

        return nextCase