from src.Case import *
from src.Plateau import *
from math import *
import random as rdm


class Agent:
    """
    Agent intelligent et autonome.
    """

    def __init__(self, id: int, type: int = 0, edges : dict = {}):
        self.id = id
        self.spawn = [22,43]
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
            self.autonomie = 10000
        elif self.type == 1:
            self.autonomie = 25000
        elif self.type == 2:
            self.autonomie = 50000
        # Setup de la charge à autonomie
        self.charge = self.autonomie
        self.isGonnaCharge: bool = False
        self.goAfterChrage : Case = None

        # Parametrage du volumeMax selon le type
        if self.type == 0:
            self.volumeMax = 15
        elif self.type == 1:
            self.volumeMax = 55
        elif self.type == 2:
            self.volumeMax = 150

        self.edges = edges

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
            self.trajet.append(plateau.getCase(self.spawn[0], self.spawn[1]))
        else:
            self.trajet = [self.trajet[self.caseOfTrajet]]
            self.caseOfTrajet = 0

        t = self.getTrajet_aStar(plateau, rdm.choice(plateau.getLieu('road')))
        for c in t:
            self.trajet.append(c)

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
        trajet = [self.trajet[self.caseOfTrajet]]
        done = 0
        if destination.isReachable():
            if trajet[done].type != 'road':
                trajet.append(plateau.nearRoads(trajet[done])[0])
                done += 1
            
            queue: list[tuple(int, Case)] = [(0, trajet[-1])]
            cout = {}
            cout[trajet[done]] = 0

            edges = self.edges
            
            # Génération plus court chemin
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
                
            pathing : list[Case] = [trajet[len(trajet)-1]]
            inPath = 0
            for i in range(len(trajet)-2, -1, -1):
                if trajet[i] in plateau.nearLieu(pathing[inPath]) or trajet[i] in plateau.nearRoads(pathing[inPath]):
                    pathing.append(trajet[i])
                    inPath += 1
            pathing.reverse()

            return pathing
        else :
            return trajet

    # ~~~~~~~~~~~~      CHECKS      ~~~~~~~~~~~~~~

    def OLD_checkNeedCharge(self, plateau) -> bool:
        """
        Vérifie le pourcentage de batterie réstant
        et rétourne True ou False en fonction de la charge.
        """
        toReach = (len(self.trajet) - self.caseOfTrajet)
        if self.isGonnaCharge:
            return False
        elif self.charge - (toReach * 50) > 0:
            tempTrj = self.trajet
            tempCoT = self.caseOfTrajet

            crgr = plateau.getLieu('charge')
            toGo : Case = None
            for c in crgr:
                if c.isReachable():
                    toGo = c

            self.trajet = [self.trajet[-1]]
            self.caseOfTrajet = 0
            destToChrage = len(self.getTrajet_aStar(plateau, toGo))
            self.trajet = tempTrj
            self.caseOfTrajet = tempCoT

            if self.charge - (toReach * 50) - destToChrage > 0:
                return False
            else :
                return True

    def checkNeedCharge(self) -> bool:
        """
        Vérifie le pourcentage de batterie réstant
        et rétourne True ou False en fonction de la charge.
        """
        toReach = (len(self.trajet) - self.caseOfTrajet)
        if self.isGonnaCharge:
            return False
        elif self.charge <= 2500:
            return True

    def checkChargeDone(self) -> bool :
        return self.charge == self.autonomie

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

    def moveT1(self, plateau: Plateau):
        """
        Module de Agent.move()
        Gere le trajet en cas de besoin de recharge.
        """
        crgr = plateau.getLieu('charge')
        toGo : Case = None
        for c in crgr:
            if c.isReachable():
                toGo = c

        trj = self.getTrajet_aStar(plateau, toGo)
        
        self.goAfterChrage = self.trajet[-1]
        self.trajet = trj
        self.caseOfTrajet = 0
        self.isGonnaCharge = True
    def moveT2(self):
        """
        Module de Agent.move()
        Gere le mouvement dans le cas ou Agent est en chargement.
        """
        if self.trajet[self.caseOfTrajet].getType() == 'charge' :
            if not self.checkChargeDone() :
                self.charging()
        else :
            if self.caseOfTrajet + self.speed < len(self.trajet):
                self.charge -= 50 * self.speed
                self.caseOfTrajet += self.speed

            elif self.caseOfTrajet + self.speed >= len(self.trajet):
                self.charge -= 50 * (len(self.trajet) - self.caseOfTrajet - 1)
                self.trajet = [self.trajet[-1]]
                self.caseOfTrajet = 0
    def moveTEnd(self, plateau: Plateau):
        """
        Module de Agent.move()
        Gere le trajet si aucun parametre blocant.
        """
        if self.goAfterChrage :
            self.trajet = self.getTrajet_aStar(plateau, self.goAfterChrage)
            self.caseOfTrajet = 0
            self.goAfterChrage = None

        if self.caseOfTrajet + self.speed < len(self.trajet):
            self.charge -= 50 * self.speed
            self.caseOfTrajet += self.speed

        elif self.caseOfTrajet + self.speed >= len(self.trajet):
            self.charge -= 50 * (len(self.trajet) - self.caseOfTrajet - 1)
            self.trajet = [self.trajet[-1]]
            self.caseOfTrajet = 0
    def move(self, plateau: Plateau) -> None:
        """
        Change la position de l'Agent sur la
        prochaine Case de son trajet.

        Gère la charge de l'Agent.
        """
        # Verification du niveau de charge
        needCharge = self.checkNeedCharge()
        if len(self.trajet) > 1 :
            if needCharge:
                self.moveT1(plateau)

            elif self.isGonnaCharge :
                self.moveT2()

            else :
                self.moveTEnd(plateau)

        else :
            self.goToRandom(plateau)

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

    # ~~~~~~~~~~      CHARGEMENT      ~~~~~~~~~~~~

    def charging(self):
        crgParTour = 200
        if self.charge + crgParTour < self.autonomie:
            self.charge += crgParTour
        else : 
            self.charge = self.autonomie
            self.isGonnaCharge = False

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~