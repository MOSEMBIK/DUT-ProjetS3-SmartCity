from src.Case import *
from src.Plateau import *
from math import *
import random as rdm

class Tache:

    def __init__(self):
        self.depart : Case = None
        self.arrive : Case = None

        self.itineraire = self.Itineraire_aStar(self.arrive)
        self.lenght = len(self.itineraire)
        
        self.volume : int = 0

        self.recompense : int = 0
        self.enCours : bool = False
    
    def demandeTache():
        # Corps à completer
        return None
    
    def setRecompense(self, newRecompense):
        self.recompense = newRecompense
        return None

    def Itineraire_aStar(self, plateau: Plateau, destination: Case) -> list:
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

