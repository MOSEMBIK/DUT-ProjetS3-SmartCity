from src.Case import *
from src.Plateau import *
from math import *
import collections
import random as rdm

class Agent:

    def __init__(self, id: int, type: int = 0):
        self.id = id
        if (type in [0, 1, 2]) :
            self.type = type

        self.visibility : bool = True

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
        self.caseOfTrajet : int = 0
        self.trajet : list[Case] = [] 

        # Setup du score à 0
        self.score : int = 0

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~















    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~      METHODES      ~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





    # ~~~~~~~~~~~~~      TRAJET      ~~~~~~~~~~~~~~~

    def setRandomTrajet(self, plateau: Plateau) -> None:
        """
        Génère un trajet aléatoire de 0 à 99 déplacements.
        """
        if self.trajet == []:
            self.trajet.append(rdm.choice(plateau.getLieu('road')))
        else:
            self.trajet = [self.trajet[self.caseOfTrajet]]
            self.caseOfTrajet = 0

        for i in range(randint(100, 250)):
            self.trajet.append(rdm.choice(plateau.nearRoads(self.trajet[i])))

        return None


    def setTrajet(self, trajet : list) -> None:
        self.trajet = trajet
        self.caseOfTrajet = 0

        return None


    def OLD_getTrajet_aStar(self, plateau: Plateau, destination: Case) -> list:
        """
        Génère le trajet le plus court vers
        une Case donnée en utilisant la methode
        type de l'algorithme a*.
        """
        queue = collections.deque()

        trajet = [self.trajet[self.caseOfTrajet]]
        done = 0

        bannedCase = []
        crashCase = []

        # Case de départ
        startXY = self.trajet[self.caseOfTrajet].getCoords()
        # Case d'arrivée
        endXY = destination.getCoords()

        # Distances départ->arrivé
        manhattanDist = abs(endXY[0]-startXY[0]) + abs(endXY[1]-startXY[1])
        pytagoreDist = sqrt(abs(endXY[0]-startXY[0])**2 + abs(endXY[1]-startXY[1])**2)
        toDo = manhattanDist + pytagoreDist

        # Génération plus court chemin
        while queue :
            print("coord : ",trajet[done].getCoords())
            dist = []
            nearRoads = plateau.nearRoads(trajet[done])
            nearLieu = plateau.nearLieu(trajet[done])

            a = set()

            try :
                print("nearlieu : ",nearLieu)
                for l in range(len(nearLieu)):
                    print("coord nearlieu : ",nearLieu[l].getCoords())
                    
                bannedCase.append(trajet[done])

                # Test si destination accessible
                nearLieuCoo = []
                for lu in nearLieu:
                    nearLieuCoo.append(lu.getCoords())
                if destination.getCoords() in nearLieuCoo :
                    # Prochaine case = destination
                    trajet.append(destination)
                    # Distance réstante = 0
                    toDo = 0

                else :

                    # On interdit les cases bannies                
                    print("nearRcs : ", nearRoads)
                    for rc in nearRoads:
                        for bC in bannedCase:
                            if plateau.isEqualCase(rc, bC):
                                nearRoads.remove(rc)

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
                print("dist : ",toDo)
            except :
                crashCase.append(bannedCase[-1])

                trajet = [self.trajet[self.caseOfTrajet]]
                done = 0
                startXY = self.trajet[self.caseOfTrajet].getCoords()
                endXY = destination.getCoords()
                manhattanDist = abs(endXY[0]-startXY[0]) + abs(endXY[1]-startXY[1])
                pytagoreDist = sqrt(abs(endXY[0]-startXY[0])**2 + abs(endXY[1]-startXY[1])**2)
                toDo = manhattanDist + pytagoreDist

                bannedCase = []
                for c in crashCase:
                    bannedCase.append(c)

                pass
        
        return trajet

    def getTrajet_aStar(self, plateau: Plateau, destination: Case) -> list:
        
        """
        Génère le trajet le plus court vers
        une Case donnée en utilisant la methode
        type de l'algorithme a*.
        """
        queue = []

        # Case de départ
        startXY = self.trajet[self.caseOfTrajet].getCoords()
        # Case d'arrivée
        endXY = destination.getCoords()

        trajet = [self.trajet[self.caseOfTrajet]]
        done = 0
        cout = {}
        cout[trajet[done]] = 0

        edges = {}
        roads = plateau.getLieu('road')
        for rCase in roads:
            nRC = plateau.nearRoads(rCase)
            nLC = plateau.nearLieu(rCase)
            if nLC :
                for lCC in nLC :
                    if plateau.isEqualCase(destination, lCC):
                        nRC.append(lCC)
            edges[rCase] = nRC
        print("Graph : ",edges)

        # Distances départ->arrivé (manhattanDist)
        toDo = abs(endXY[0]-startXY[0]) + abs(endXY[1]-startXY[1])

        # Génération plus court chemin
        while queue :
            print("Distance restante : ",toDo)
            print("Coordonnees : ",trajet[done].getCoords())

            if 
            toDo = 0

        return trajet


    def getTrajet_dijkstra(self, plateau: Plateau, destination: Case) -> list:
        """
        Génère le trajet le plus court vers
        une Case donnée.
        """
        trajet = [self.trajet[self.caseOfTrajet]]
        done = 0

        roads = plateau.getLieu('road')
        # Génération plus court chemin

        return trajet

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~















    # ~~~~~~~~~~~~      CHECKS      ~~~~~~~~~~~~~~

    def checkNeedCharge(self) -> bool:
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


    def move(self, plateau: Plateau) -> None:
        """
        Change la position de l'Agent sur la
        prochaine Case de son trajet.

        Gère la charge de l'Agent.
        """
        # Verification du niveau de charge
        needCharge = self.checkNeedCharge()

        if not(needCharge) :
            if self.caseOfTrajet + self.speed < len(self.trajet):
                self.charge -= 50 * self.speed
                self.caseOfTrajet += self.speed

            elif self.caseOfTrajet + self.speed >= len(self.trajet):
                self.charge -= 50 * (len(self.trajet) - self.caseOfTrajet - 1)
                self.trajet = [self.trajet[self.caseOfTrajet]]
                self.caseOfTrajet = 0

        else :
            crgr = plateau.getLieu('charge')
            toGo = Case
            for c in crgr :
                if c.isReachable() :
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