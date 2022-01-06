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
    nbAgentE1 = 1
    nbAgentE2 = 1
    heuristiqueE1 = 0
    heuristiqueE2 = 0

    choixTacheE1 = 1
    choixTacheE2 = 1

    nbTaches = 50
    nbTacheSim = 10

    window = SimMenu()
    window.start()

    return nbAgentE1, nbAgentE2, heuristiqueE1, heuristiqueE2, choixTacheE1, choixTacheE2, nbTaches, nbTacheSim

def main(val):
    print(val)
    sim: Simulation = Simulation(name="SmartCity - MARS", ico='img/logo/smartCorp.png', nbAgentE1=1, nbAgentE2=1, heuristiqueE1=0, heuristiqueE2=1, choixTacheE1=1, choixTacheE2=1, nbTaches=5, nbTachesSim=1)
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

                if ag.tacheToDo :
                    if ag.tacheToDo.enCours :
                        allDone = False
                    else :
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


if __name__ == "__main__" :
    val = 0
    preMain()
    main(val)