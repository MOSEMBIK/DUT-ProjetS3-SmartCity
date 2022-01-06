import time
from random import *
from src.Simulation import *
from src.Interface import *

from src.Plateau import *
from src.Case import *
from src.SimMenu import *

from tkinter import *
from PIL import ImageTk, Image


def preMain():
    # 0 = manathan
    # 1 = pythagore
    # 2 = dijkstra

    # 0 = random
    # 1 = rentable

    window = SimMenu()
    window.start()
    nbAgentE1 = window.nbAgentE1
    nbAgentE2 = window.nbAgentE2
    nbTaches = window.nbTaches
    heuristiqueE1 = window.heuristiqueE1
    heuristiqueE2 = window.heuristiqueE2
    choixTacheE1 = window.choixTacheE1
    choixTacheE2 = window.choixTacheE2

    print("nb Agent Equipe 1 : ", nbAgentE1)
    print("nb Agent Equipe 2 : ", nbAgentE2)
    print("Nb de taches : ", nbTaches)
    print("Heuristique equipe 1 : ", heuristiqueE1)
    print("Heuristique equipe 2 : ", heuristiqueE2)
    print("Choix tache equipe 1 : ", choixTacheE1)
    print("Choix tache equipe 2 : ", choixTacheE2)

    return nbAgentE1, nbAgentE2, heuristiqueE1, heuristiqueE2, nbTaches, choixTacheE1, choixTacheE2


def main(val):
    print(val)
    sim: Simulation = Simulation(name="SmartCity - MARS", ico='img/logo/smartCorp.png', nbAgentE1=2, nbAgentE2=2,
                                 heuristiqueE1=0, heuristiqueE2=1, nbTaches=50, nbTachesSim=10)
    mapS = sim.plt.itf.skins_map_update(sim.plt.canvas, None, None)

    sim.allGoToRandom()

    allDone = False

    while len(sim.taches) > 0 or len(sim.plt.listeTaches) > 0 or allDone:
        if len(sim.plt.listeTaches) <= 4:
            for i in range(6):
                if len(sim.plt.listeTaches) > 1:
                    t = rdm.choice(sim.taches)
                    sim.plt.listeTaches.append(t)
                    sim.taches.pop(sim.taches.index(t))
                if len(sim.plt.listeTaches) == 1:
                    t = sim.taches[0]
                    sim.plt.listeTaches.append(t)
                    sim.taches.pop(0)

        skins = []

        sim.allMove()
        for e in range(len(sim.equipe)):
            for a in sim.equipe[e].getAgents():
                ag: Agent = sim.equipe[e].getAgents()[a]
                sim.layer.updateTab(ag)
                sim.layer.updateScore()

                Interface.imageMove(sim.plt.canvas, sim.skin.get(ag), ag.trajet[ag.caseOfTrajet].getCoords())
                skins.append(sim.skin.get(ag))
                # sim.plt.itf.moveSkin(sim.skin.get(ag), ag.trajet[ag.caseOfTrajet].getCoords())
                # print("E :", sim.equipe[e].id, "A :", 1 + ag.id, ag.trajet[ag.caseOfTrajet].getCoords())

                if ag.tacheToDo:
                    if ag.tacheToDo.enCours:
                        allDone = False
                    else:
                        allDone = True

        # Update du screen, affichage du design de map, pause du programme
        mapS = sim.plt.itf.skins_map_update(sim.plt.canvas, mapS, skins)
        time.sleep(0.02)

    time.sleep(5)
    print("END")

    sim.plt.delcv()
    sim.plt.itf.gameFini(sim.layer.getWinner())
    sim.plt.start()
    return None


if __name__ == "__main__":
    val = 0
    preMain()
    main(val)
