from src.Environnement import *
from src.Case import *
from math import *

class Agent:

    def __init__(self, id: int, type: int):
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
        if self.trajet == []:
            self.trajet.append(random.choice(environnement.getLieu('road')))
        else:
            self.trajet = [self.trajet[self.caseOfTrajet]]
            self.caseOfTrajet = 0

        for i in range(randint(100)):
            self.trajet.append(random.choice(environnement.nearRoads(self.trajet[i])))

        return None


    def initTrajet_aStar(self, environnement: Environnement, destination: Case) -> None:
        """
        Génère le trajet le plus court vers
        une Case donnée en utilisant la methode
        type de l'algorithme a*.
        """
        # Case de départ
        startXY = self.trajet[self.caseOfTrajet].getCoords()
        # Case d'arrivée
        endXY = destination.getCoords()
        
        # Clear du dernier trajet
        self.trajet = [self.trajet[self.caseOfTrajet]]
        self.caseOfTrajet = 0

        # Distances départ->arrivé
        manhattanDist = abs(endXY[0]-startXY[0]) + abs(endXY[1]-startXY[1])
        pytagoreDist = sqrt(abs(endXY[0]-startXY[0])**2 + abs(endXY[1]-startXY[1])**2)
        toDo = manhattanDist + pytagoreDist

        # Distance parcourue
        done = 0

        # Génération plus court chemin
        while toDo != 0 :
            dist = []
            nearRoads = environnement.nearRoads(self.trajet[self.caseOfTrajet])
            nearLieu = environnement.nearLieux(self.trajet[self.caseOfTrajet])

            # Test si destination accessible
            if destination in nearLieu :
                # Prochaine case = destination
                self.trajet.append(destination)
                # Distance réstante = 0
                toDo = 0

            else :
                # On empèche le retour en arrière
                nearRoads.remove(self.trajet[done])

                # Pour chaque Route
                for nC in nearRoads :
                    nCXY = nC.getCoords()

                    # Calcul des distances
                    manhattanDist = abs(endXY[0]-nCXY[0]) + abs(endXY[1]-nCXY[1])
                    pytagoreDist = sqrt(abs(endXY[0]-nCXY[0])**2 + abs(endXY[1]-nCXY[1])**2)
                    dist.append(manhattanDist + pytagoreDist)

                # Ajout au trajet de la case minimisant la distance réstante
                self.trajet.append( nearRoads[dist.index(min(dist))] )
                done += 1

                # Modification de la distance réstante
                startXY = self.trajet[done].getCoords()
                toDo = abs(endXY[0]-startXY[0]) + abs(endXY[1]-startXY[1])
        
        return None

    def initTrajet_dijkstra(self, environnement: Environnement, destinationId : int, destination: Case) -> None:
        """
        Génère le trajet le plus court vers
        une Case donnée.
        """
        roads = environnement.getLieu('road')
        # Génération plus court chemin

        return None