from src.Case import *
from src.Environnement import *
from math import *
import random as rdm

class Agent:

    def __init__(self, id: int, type: int = 0):
        self.id = id
        # Test de la validité du type
        try :
            if (type in (0, 2)) :
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
        # Setup de la charge à autonomie
        self.charge = self.autonomie

        # Parametrage du volumeMax selon le type
        if (self.type == 0) :
            self.volumeMax = 15
        elif (self.type == 1) :
            self.volumeMax = 55
        elif (self.type == 2) :
            self.volumeMax = 150

        # Setup de la position à Null
        self.caseOfTrajet = 0
        self.trajet = [Case]

        # Setup du score à 0
        self.score = 0

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~















    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~      METHODES      ~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





    # ~~~~~~~~~~~~~      TRAJET      ~~~~~~~~~~~~~~~

    def setRandomTrajet(self, environnement: Environnement) -> None:
        """
        Génère un trajet aléatoire de 0 à 99 déplacements.
        """
        if self.trajet == []:
            self.trajet.append(rdm.choice(environnement.getLieu('road')))
        else:
            self.trajet = [self.trajet[self.caseOfTrajet]]
            self.caseOfTrajet = 0

        for i in range(randint(100)):
            self.trajet.append(rdm.choice(environnement.nearRoads(self.trajet[i])))

        return None


    def setTrajet(self, trajet : list) -> None:
        self.trajet = trajet
        self.caseOfTrajet = 0

        return None


    def getTrajet_aStar(self, environnement: Environnement, destination: Case) -> list:
        """
        Génère le trajet le plus court vers
        une Case donnée en utilisant la methode
        type de l'algorithme a*.
        """
        trajet = [self.trajet[self.caseOfTrajet]]
        done = 0

        # Case de départ
        startXY = self.trajet[self.caseOfTrajet].getCoords()
        # Case d'arrivée
        endXY = destination.getCoords()

        # Distances départ->arrivé
        manhattanDist = abs(endXY[0]-startXY[0]) + abs(endXY[1]-startXY[1])
        pytagoreDist = sqrt(abs(endXY[0]-startXY[0])**2 + abs(endXY[1]-startXY[1])**2)
        toDo = manhattanDist + pytagoreDist

        # Génération plus court chemin
        while toDo != 0 :
            dist = []
            nearRoads = environnement.nearRoads(trajet[done])
            nearLieu = environnement.nearLieux(trajet[done])

            # Test si destination accessible
            if destination in nearLieu :
                # Prochaine case = destination
                trajet.append(destination)
                # Distance réstante = 0
                toDo = 0

            else :
                # On empèche le retour en arrière
                nearRoads.remove(trajet[done])

                # Pour chaque Route
                for nC in nearRoads :
                    nCXY = nC.getCoords()

                    # Calcul des distances
                    manhattanDist = abs(endXY[0]-nCXY[0]) + abs(endXY[1]-nCXY[1])
                    pytagoreDist = sqrt(abs(endXY[0]-nCXY[0])**2 + abs(endXY[1]-nCXY[1])**2)
                    dist.append(manhattanDist + pytagoreDist)

                # Ajout au trajet de la case minimisant la distance réstante
                trajet.append( nearRoads[dist.index(min(dist))] )
                done += 1

                # Modification de la distance réstante
                startXY = trajet[done].getCoords()
                toDo = abs(endXY[0]-startXY[0]) + abs(endXY[1]-startXY[1])
        
        return trajet


    def getTrajet_dijkstra(self, environnement: Environnement, destination: Case) -> list:
        """
        Génère le trajet le plus court vers
        une Case donnée.
        """
        trajet = [self.trajet[self.caseOfTrajet]]
        done = 0

        roads = environnement.getLieu('road')
        # Génération plus court chemin

        return trajet

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~















    # ~~~~~~~~~~~~      CHECKS      ~~~~~~~~~~~~~~

    def checkNeedCharge(self, environnement : Environnement) -> bool:
        """
        Vérifie le pourcentage de batterie réstant
        et rétourne True ou False en fonction de la charge.
        """
        percentDone = ((len(self.trajet) - self.caseOfTrajet) * 100 ) / len(self.trajet)

        if ( ( (self.charge * 100) / self.autonomie ) <= 0.25 ) :
            if percentDone >= 0.8 :
                return False
            else :
                return True
        else :
            return False















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


    def move(self, environnement: Environnement) -> None:
        """
        Change la position de l'Agent sur la
        prochaine Case de son trajet.

        Gère la charge de l'Agent.
        """
        # Verification du niveau de charge
        needCharge = self.checkNeedCharge(environnement)

        if needCharge :
            if self.caseOfTrajet + self.speed < len(self.trajet):
                self.charge -= 50 * self.speed
                self.caseOfTrajet += self.speed

            elif self.caseOfTrajet + self.speed >= len(self.trajet):
                self.charge -= 50 * (len(self.trajet) - self.caseOfTrajet - 1)
                self.trajet = [self.trajet[self.caseOfTrajet]]
                self.caseOfTrajet = 0

        else :
            self.setTrajet(self.getTrajet_aStar(environnement, environnement.getLieu('charge')))

        return None

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~