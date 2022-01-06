from src.Case import *
import src.Plateau as Plateau
from math import *
import random as rdm


class Tache:

    def __init__(self, dpt: Case, arv: Case, volume: float, plat: Plateau, heuristiqueE1=0, heuristiqueE2=0):
        self.depart: Case = dpt
        self.arrivee: Case = arv
        self.volume: float = volume

        self.itineraireE1 = self.Itineraire_aStar(plat, self.arrivee, heuristiqueE1)
        self.itineraireE2 = self.Itineraire_aStar(plat, self.arrivee, heuristiqueE2)
        self.length = int((len(self.itineraireE1) + len(self.itineraireE2))/2)

        self.chargeNeeded : int = int(self.length * 50 * (1+self.volume/100))

        self.recompense: int = int(self.volume * self.length * (random() * 0.5 + 1))

        self.rentabilite = (self.recompense / self.length)/self.volume

        self.enCours: bool = False

    def Itineraire_aStar_Manatthan(self, plateau: Plateau, destination: Case) -> list:
        """
        Génère le trajet le plus court vers
        une Case donnée en utilisant la methode
        type de l'algorithme a*.
        """
        trajet = [self.depart]
        done = 0
        if destination.isReachable():
            if trajet[done].type != 'road':
                trajet.append(plateau.nearRoads(trajet[done])[0])
                done += 1

            queue: list[tuple(int, Case)] = [(0, trajet[-1])]
            cout = {}
            cout[trajet[done]] = 0

            edges = plateau.edges

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

            pathing: list[Case] = [trajet[len(trajet) - 1]]
            inPath = 0
            for i in range(len(trajet) - 2, -1, -1):
                if trajet[i] in plateau.nearLieu(pathing[inPath]) or trajet[i] in plateau.nearRoads(pathing[inPath]):
                    pathing.append(trajet[i])
                    inPath += 1
            pathing.reverse()

            return pathing
        else:
            return trajet

    def Itineraire_aStar_Pythagore(self, plateau: Plateau, destination: Case) -> list:
        """
        Génère le trajet le plus court vers
        une Case donnée en utilisant la methode
        type de l'algorithme a*.
        """
        trajet = [self.depart]
        done = 0
        if destination.isReachable():
            if trajet[done].type != 'road':
                trajet.append(plateau.nearRoads(trajet[done])[0])
                done += 1

            queue: list[tuple(int, Case)] = [(0, trajet[-1])]
            cout = {}
            cout[trajet[done]] = 0

            edges = plateau.edges

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
                        prio = nCout + sqrt(abs(destination.getCoords()[0] - nCXY[0])**2 + abs(destination.getCoords()[1] - nCXY[1])**2)
                        queue.append((prio, next))
                        trajet.append(current)
                        done += 1

            pathing: list[Case] = [trajet[len(trajet) - 1]]
            inPath = 0
            for i in range(len(trajet) - 2, -1, -1):
                if trajet[i] in plateau.nearLieu(pathing[inPath]) or trajet[i] in plateau.nearRoads(pathing[inPath]):
                    pathing.append(trajet[i])
                    inPath += 1
            pathing.reverse()

            return pathing
        else:
            return trajet

    def Itineraire_aStar_Dijkstra(self, plateau: Plateau, destination: Case) -> list:
        """
        Génère le trajet le plus court vers
        une Case donnée en utilisant la methode
        type de l'algorithme a*.
        """
        trajet = [self.depart]
        done = 0
        if destination.isReachable():
            if trajet[done].type != 'road':
                trajet.append(plateau.nearRoads(trajet[done])[0])
                done += 1

            queue: list[tuple(int, Case)] = [(0, trajet[-1])]
            cout = {}
            cout[trajet[done]] = 0

            edges = plateau.edges

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
                        prio = nCout + 1
                        queue.append((prio, next))
                        trajet.append(current)
                        done += 1

            pathing: list[Case] = [trajet[len(trajet) - 1]]
            inPath = 0
            for i in range(len(trajet) - 2, -1, -1):
                if trajet[i] in plateau.nearLieu(pathing[inPath]) or trajet[i] in plateau.nearRoads(pathing[inPath]):
                    pathing.append(trajet[i])
                    inPath += 1
            pathing.reverse()

            return pathing
        else:
            return trajet

    def Itineraire_aStar(self, plateau: Plateau, destination: Case, heuristique) -> list:
    
        if heuristique == 0:
            return self.Itineraire_aStar_Manatthan(plateau, destination)
        if heuristique == 1:
            return self.Itineraire_aStar_Pythagore(plateau, destination)
        if heuristique == 2:
            return self.Itineraire_aStar_Dijkstra(plateau, destination)

    def setEnCours(self, boolean):
        self.enCours = boolean

    def getEnCours(self):
        return self.enCours
