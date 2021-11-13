from _typeshed import NoneType
from src.Environnement import *
from math import *


class Agent:

    def __init__(self, id: int, type: int):
        self.id = id
        # Test de la validité du type
        try:
            if type in (0, 2):
                self.type = type
        except:
            raise Exception("Invalid Agent.type parameter given.")

        self.visibility = True

        # Parametrage de la vitesse selon le type
        if self.type == 0:
            self.speed = 4
        elif self.type == 1:
            self.speed = 2
        elif self.type == 2:
            self.speed = 1
        # Parametrage de l'autonomie selon le type
        if self.type == 0:
            self.autonomie = 2500
        elif self.type == 1:
            self.autonomie = 5000
        elif self.type == 2:
            self.autonomie = 8000
        # Parametrage du volumeMax selon le type
        if self.type == 0:
            self.volumeMax = 15
        elif self.type == 1:
            self.volumeMax = 55
        elif (self.type == 2):
            self.volumeMax = 150

        self.caseOfTrajet = 0
        self.trajet = []

        self.score = 0

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~      METHODES      ~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def move(self) -> None:
        """
        Change la position de l'Agent sur la
        prochaine Case de son trajet.
        """
        if self.caseOfTrajet + 1 < len(self.trajet):
            self.caseOfTrajet += 1

        elif self.caseOfTrajet + 1 >= len(self.trajet):
            self.trajet = [self.trajet[self.caseOfTrajet]]
            self.caseOfTrajet = 0

        return None

    def randomTrajet(self, environnement: Environnement) -> None:
        """
        Génère un trajet aléatoire de 0 à 99 déplacements.
        """
        roads = environnement.getRoads()

        if self.trajet == []:
            startId, startCase = random.choice(list(roads.items()))
            self.trajet.append(startCase)
        else:
            onCase = self.trajet[self.caseOfTrajet]
            self.trajet = [onCase]
            self.caseOfTrajet = 0

        for i in range(randint(100)):
            nextId, nextCase = random.choice(self.trajet[i].nearRoads())
            self.trajet.append(nextCase)

        return None

    def initTrajet_aStar(self, environnement: Environnement, destinationId: int, destination: Case) -> None:
        """
        Génère le trajet le plus court vers
        une Case donnée en utilisant la methode
        type de l'algorithme a*.
        """
        lastPos = self.trajet[self.caseOfTrajet]

        startXY = self.trajet[self.caseOfTrajet].getCoordonnees()
        endXY = destination.getCoordonnees()
        manhattanDist = abs(endXY[0] - startXY[0]) + abs(endXY[1] - startXY[1])

        done = 0
        toDo = manhattanDist

        # Génération plus court chemin
        while toDo != 0:
            dist = []
            lastPos = self.trajet[done]
            nearRoads = self.trajet[self.caseOfTrajet].nearRoads()
            nearRoads.remove(lastPos)
            for nC in nearRoads:
                nCXY = nC.getCoordonnees()
                dist.append(abs(endXY[0] - nCXY[0]) + abs(endXY[1] - nCXY[1]))

            self.trajet.append(nearRoads[dist.index(min(dist))])

            # Modification de la distance
            startXY = self.trajet[self.caseOfTrajet].getCoordonnees()
            toDo = abs(endXY[0] - startXY[0]) + abs(endXY[1] - startXY[1])
            done += 1

        return None

    def initTrajet_dijkstra(self, environnement: Environnement, destinationId: int, destination: Case) -> None:
        """
        Génère le trajet le plus court vers
        une Case donnée.
        """
        roads = environnement.getRoads()

        # Génération plus court chemin

        return None
