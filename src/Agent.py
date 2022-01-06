from src.Case import *
from src.Plateau import *
from src.Tache import *
from math import *
import random as rdm


class Agent:
    """
    Agent intelligent et autonome.
    """

    def __init__(self, id: str, spawn : Case):
        self.id = id
        self.spawn : Case = spawn

        # Parametrage de la vitesse
        self.speed = 1

        # Parametrage de l'autonomie
        self.autonomie = 15000
        # Setup de la charge à autonomie
        self.charge = self.autonomie
        self.isGonnaCharge: bool = False
        self.goAfterCharge: Case = None

        # Parametrage du volumeMax
        self.volumeMax = 100

        # Setup de la position à Null
        self.caseOfTrajet: int = 0
        self.trajet: list[Case] = []

        # Tache
        self.tacheChose: Tache = None
        self.tacheToDo: Tache = None
        
        if self.tacheToDo is not None:
            self.wearing = float('%.2f'%(1 + (self.tacheToDo.volume / self.volumeMax)))
        else :
            self.wearing = 1

        # Setup du score à 0
        self.score: int = 0

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~      METHODES      ~~~~~~~~~~~~~~

    # ~~~~~~~~~~~~~      TACHES      ~~~~~~~~~~~~~~~

    def randomChooseTache(self, plateau:Plateau) -> None:
        # On choisit une tache au hasard dans la liste.
        self.tacheChose = rdm.choice(plateau.listeTaches)

        self.trajet = self.getTrajet_aStar_Mannhattan(plateau, self.tacheChose.depart)
        self.caseOfTrajet = 0

    def chooseTache(self, plateau:Plateau) -> None:
        # On choisit la tache la plus rentable
        if plateau.listeTaches != []:
            self.tacheChose = plateau.listeTaches[0]
            for i in plateau.listeTaches:
                if i.rentabilite > self.tacheChose.rentabilite :
                    self.tacheChose = i
            self.trajet = self.getTrajet_aStar_Mannhattan(plateau, self.tacheChose.depart)
            self.caseOfTrajet = 0
        else :
            self.charge = 0

    # def chooseTacheOpti2(self, pl:Plateau) -> None:
    #     # On choisit la tache la plus proche possible
    #     proche = 1000
    #     for tache in pl.listeTaches :
    #         distance = len(getTrajet_aStar_Mannhattan(self, pl, tache.depart);
    #         if (len(getTrajet_aStar_Mannhattan(self, pl, tache.depart)) < proche):
    #             if (checkNeedCharge(self)):
    #                 proche = distance
    #                 self.tacheChose = tache
    #     return None

    def takeTache(self, plateau: Plateau):
        if self.tacheChose in plateau.listeTaches:
            self.tacheToDo = self.tacheChose
            self.trajet = self.tacheToDo.itineraire
            self.caseOfTrajet = 0
            self.wearing = float('%.2f'%(1 + ((self.tacheToDo.volume / self.volumeMax))))
            plateau.listeTaches.pop(plateau.listeTaches.index(self.tacheChose))
        else :
            self.chooseTache(plateau)

    def tacheEnd(self) -> None:
        # A appeler quand l'agent est arrivé.
        self.score += self.tacheToDo.recompense
        self.tacheToDo = None
        self.tacheChose = None
        self.wearing = 1
        return None

    # ~~~~~~~~~~~~~      TRAJET      ~~~~~~~~~~~~~~~

    def setRandomTrajet(self, plateau: Plateau) -> None:
        """
        Génère un trajet aléatoire de 0 à 99 déplacements.
        """
        if not self.trajet:
            self.trajet.append(plateau.getCase(self.spawn.getCoords()[0], self.spawn.getCoords()[1]))
        else:
            self.trajet = [self.trajet[self.caseOfTrajet]]
            self.caseOfTrajet = 0

        t = self.getTrajet_aStar_Mannhattan(plateau, rdm.choice(plateau.getLieu('road')))
        for c in t:
            self.trajet.append(c)

        return None

    def setTrajet(self, trajet: list) -> None:
        self.trajet = trajet
        self.caseOfTrajet = 0

        return None

    def getTrajet_aStar_Mannhattan(self, plateau: Plateau, destination: Case) -> list:
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

    def getTrajet_aStar_Pythagore(self, plateau: Plateau, destination: Case) -> list:
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
            toGo: Case = None
            for c in crgr:
                if c.isReachable():
                    toGo = c

            self.trajet = [self.trajet[-1]]
            self.caseOfTrajet = 0
            destToChrage = len(self.getTrajet_aStar_Mannhattan(plateau, toGo))
            self.trajet = tempTrj
            self.caseOfTrajet = tempCoT

            if self.charge - (toReach * 50) - destToChrage > 0:
                return False
            else:
                return True

    def checkNeedCharge(self) -> bool:
        """
        Vérifie le pourcentage de batterie réstant
        et rétourne True ou False en fonction de la charge.
        """
        if self.isGonnaCharge:
            return False
            
        # L'agent calcule la batterie à l'arrivée, si elle est < 30%, il passera se charger pendant sa tâche
        elif self.tacheToDo and ((self.charge - self.tacheToDo.chargeNeeded) < self.autonomie*0.3):
                return True

        elif self.charge <= self.autonomie*0.3:
            return True


    def checkChargeDone(self) -> bool:
        return self.charge == self.autonomie

    def checkAccesTache(self, plateau: Plateau) -> bool:
        if self.tacheChose:
            if self.tacheChose in plateau.listeTaches:
                if self.tacheToDo and self.tacheChose == self.tacheToDo:
                    return False
                else:
                    return True
            else:
                if self.tacheToDo and self.tacheChose == self.tacheToDo:
                    return True
                else :
                    return False
        else:
            return False

    def checkEndTache(self) -> bool:
        if self.trajet[self.caseOfTrajet] == self.tacheToDo.arrivee:
            return True
        else:
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

    def moveT1(self, plateau: Plateau):
        """
        Module de Agent.move()
        Gere le trajet en cas de besoin de recharge.
        """
        Zcharge :list[Case] = plateau.getLieu('Zone de recharge')
        toGo = None
        for zch in Zcharge:
            trj = self.getTrajet_aStar_Mannhattan(plateau, zch)
            if toGo != None :
                if len(trj) < len(toGo) :
                    toGo = trj
            else :
                toGo = trj

        self.goAfterCharge = self.trajet[-1]
        self.trajet = toGo
        self.caseOfTrajet = 0
        self.isGonnaCharge = True

    def moveT2(self):
        """
        Module de Agent.move()
        Gere le mouvement dans le cas ou Agent est en chargement.
        """
        if self.trajet[self.caseOfTrajet].getType() == 'Zone de recharge':
            if not self.checkChargeDone():
                self.charging()
        else:
            if self.caseOfTrajet + self.speed < len(self.trajet):
                self.charge -= int(50 * self.wearing)
                self.caseOfTrajet += self.speed

            elif self.caseOfTrajet + self.speed >= len(self.trajet):
                self.charge -= int(50 * self.wearing)
                self.trajet = [self.trajet[-1]]
                self.caseOfTrajet = 0

    def moveTEnd(self, plateau: Plateau):
        """
        Module de Agent.move()
        Gere le trajet si aucun parametre blocant.
        """
        if self.goAfterCharge:
            self.trajet = self.getTrajet_aStar_Mannhattan(plateau, self.goAfterCharge)
            self.caseOfTrajet = 0
            self.goAfterCharge = None

        if self.caseOfTrajet + self.speed < len(self.trajet):
            self.charge -= int(50 * self.wearing)
            self.caseOfTrajet += self.speed

        elif self.caseOfTrajet + self.speed >= len(self.trajet):
            self.charge -= int(50 * self.wearing)
            self.trajet = [self.trajet[-1]]
            self.caseOfTrajet = 0

    def move(self, plateau: Plateau) -> None:
        """
        Change la position de l'Agent sur la
        prochaine Case de son trajet.

        Gère la charge de l'Agent.
        """
        if self.charge > 0:
            # Verification du niveau de charge
            needCharge = self.checkNeedCharge()
            if len(self.trajet) > 1:
                if needCharge:
                    self.moveT1(plateau)
                elif self.isGonnaCharge:
                    self.moveT2()
                else:
                    self.moveTEnd(plateau)
            else:
                self.goToRandom(plateau)
        return None

    def move2(self, plateau: Plateau) -> None:
        """
        Change la position de l'Agent sur la
        prochaine Case de son trajet.

        Gestion complète.
        """
        # Verification du niveau de charge

        if self.charge > 0:
            if self.trajet[self.caseOfTrajet] != self.trajet[-1] :
                if self.tacheChose:
                    if self.checkAccesTache(plateau):
                        if self.checkNeedCharge() and not(self.isGonnaCharge):
                            self.moveT1(plateau)

                        elif self.isGonnaCharge:
                            self.moveT2()

                        else:
                            self.moveTEnd(plateau)
                    else:
                        self.chooseTache(plateau)
                else:
                    self.chooseTache(plateau)

            elif self.isGonnaCharge:
                    self.moveT2()

            else:
                if self.tacheChose:
                    if self.trajet[self.caseOfTrajet] == self.tacheChose.depart:
                        self.takeTache(plateau)
                    else :
                        self.moveTEnd(plateau)

                if self.tacheToDo :
                    if self.checkEndTache():
                        self.tacheEnd()
                        self.chooseTache(plateau)
                else:
                    self.chooseTache(plateau)
        elif self.trajet[self.caseOfTrajet].getType() == 'Zone de recharge':
            if not self.checkChargeDone():
                self.charging()

        return None

    def goTo(self, plateau: Plateau, destination: Case) -> None:
        """
        Envoie un agent vers une direction.
        """
        self.setTrajet(self.getTrajet_aStar_Mannhattan(plateau, destination))
        return None

    def goToRandom(self, plateau: Plateau) -> None:
        """
        Envoie un agent vers une direction.
        """
        self.setRandomTrajet(plateau)
        self.randomChooseTache(plateau)
        return None

    # ~~~~~~~~~~      CHARGEMENT      ~~~~~~~~~~~~

    def charging(self):
        crgParTour = 700
        if self.charge + crgParTour < self.autonomie:
            self.charge += crgParTour
        else:
            self.charge = self.autonomie
            self.isGonnaCharge = False

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
