from src.Case import *
from src.Plateau import *
from math import *
import random as rdm


class Agent:
    """
    Agent intelligent et autonome.
    """

    def __init__(self, id: int, type: int = 0):
        self.id = id
        if type in [0, 1, 2]:
            self.type = type

        self.visibility: bool = True

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
        # Setup de la charge à autonomie
        self.charge = self.autonomie

        # Parametrage du volumeMax selon le type
        if self.type == 0:
            self.volumeMax = 15
        elif self.type == 1:
            self.volumeMax = 55
        elif self.type == 2:
            self.volumeMax = 150

        # Setup de la position à Null
        self.caseOfTrajet: int = 0
        self.trajet: list[Case] = []

        # Setup du score à 0
        self.score: int = 0

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~      METHODES      ~~~~~~~~~~~~~~

    # ~~~~~~~~~~~~~      TRAJET      ~~~~~~~~~~~~~~~

    def setRandomTrajet(self, plateau: Plateau) -> None:
        """
        Génère un trajet aléatoire de 0 à 99 déplacements.
        """
        if not self.trajet:
            self.trajet.append(rdm.choice(plateau.getLieu('road')))
        else:
            self.trajet = [self.trajet[self.caseOfTrajet]]
            self.caseOfTrajet = 0

        for i in range(randint(100, 250)):
            self.trajet.append(rdm.choice(plateau.nearRoads(self.trajet[i])))

        return None

    def setTrajet(self, trajet: list) -> None:
        self.trajet = trajet
        self.caseOfTrajet = 0

        return None

    def getTrajet_aStar(self, plateau: Plateau, destination: Case) -> list:

        """
        Génère le trajet le plus court vers
        une Case donnée en utilisant la methode
        type de l'algorithme a*.
        """
        queue: list[tuple(int, Case)] = [(0, self.trajet[self.caseOfTrajet])]

        trajet = [self.trajet[self.caseOfTrajet]]
        done = 0
        cout = {}
        cout[trajet[done]] = 0

        edges = {}
        roads = plateau.getLieu('road')
        for rCase in roads:
            nRC = plateau.nearRoads(rCase)
            nLC = plateau.nearLieu(rCase)
            if nLC:
                for lCC in nLC:
                    if plateau.isEqualCase(destination, lCC):
                        nRC.append(lCC)
            edges[rCase] = nRC
        
        # Génération plus court chemin
        print("Start : ",trajet[done].getCoords())
        while queue:
            # Recuperation de la case optimale
            idx = 0
            for i in range(1, len(queue)):
                if queue[idx][0] > queue[i][0]:
                    idx = i
            current = queue[idx][1]
            queue.remove(queue[idx])

            # Gestion de l'arrivee
            if plateau.isEqualCase(current, destination):
                trajet.append(destination)
                break

            # Generation du trajet
            for next in edges[current]:
                nCout = cout[current]  
                if next not in cout or nCout < cout[next]:
                    cout[next] = nCout
                    nCXY = current.getCoords()
                    prio = nCout + abs(destination.getCoords()[0] - nCXY[0]) + abs(destination.getCoords()[1] - nCXY[1])
                    queue.append((prio, next))
                    trajet.append(current)
                    done += 1

            print("Coords : ",trajet[done].getCoords())
        print("End : ",trajet[done+1].getCoords())
        return trajet

    # ~~~~~~~~~~~~      CHECKS      ~~~~~~~~~~~~~~

    def checkNeedCharge(self) -> bool:
        """
        Vérifie le pourcentage de batterie réstant
        et rétourne True ou False en fonction de la charge.
        """
        percentDone = ((len(self.trajet) - self.caseOfTrajet) * 100) / len(self.trajet)
        return (((self.charge * 100) / self.autonomie) <= 0.25 and percentDone >= 0.8)

    # ~~~~~~~~~~      DEPLACEMENTS      ~~~~~~~~~~~~

    def moveSimple(self) -> None:
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

    def move(self, plateau: Plateau) -> None:
        """
        Change la position de l'Agent sur la
        prochaine Case de son trajet.

        Gère la charge de l'Agent.
        """
        # Verification du niveau de charge
        needCharge = self.checkNeedCharge()

        if not (needCharge):
            if self.caseOfTrajet + self.speed < len(self.trajet):
                self.charge -= 50 * self.speed
                self.caseOfTrajet += self.speed

            elif self.caseOfTrajet + self.speed >= len(self.trajet):
                self.charge -= 50 * (len(self.trajet) - self.caseOfTrajet - 1)
                self.trajet = [self.trajet[self.caseOfTrajet]]
                self.caseOfTrajet = 0

        else:
            crgr = plateau.getLieu('charge')
            toGo = Case
            for c in crgr:
                if c.isReachable():
                    toGo = c
            self.setTrajet(self.getTrajet_aStar(plateau, toGo))

        return None

    def goTo(self, plateau: Plateau, destination: Case) -> None:
        """
        Envoie un agent vers une direction.
        """
        self.setTrajet(self.getTrajet_aStar(plateau, destination))
        return None

    def goToRandom(self, plateau: Plateau) -> None:
        """
        Envoie un agent vers une direction.
        """
        self.setRandomTrajet(plateau)
        return None

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~