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
    heuristiqueE1 = 1
    heuristiqueE2 = 0

    choixTacheE1 = 1
    choixTacheE2 = 1

    nbTaches = 2
    nbTacheSim = 1

    window = SimMenu()
    window.start()

    return nbAgentE1, nbAgentE2, heuristiqueE1, heuristiqueE2, choixTacheE1, choixTacheE2, nbTaches, nbTacheSim

def main(nbAgentE1, nbAgentE2, heuristiqueE1, heuristiqueE2, choixTacheE1, choixTacheE2, nbTaches, nbTacheSim):
    sim: Simulation = Simulation(name="SmartCity - MARS", ico='img/logo/smartCorp.png', nbAgentE1=nbAgentE1, nbAgentE2=nbAgentE2, heuristiqueE1=heuristiqueE1, heuristiqueE2=heuristiqueE2, choixTacheE1=choixTacheE1, choixTacheE2=choixTacheE2, nbTaches=nbTaches, nbTachesSim=nbTacheSim)
    mapS = sim.plt.itf.skins_map_update(sim.plt.canvas, None, None)

    sim.allGoToRandom()

    allDone = False
    tour = 1
    while len(sim.taches) > 0 or len(sim.plt.listeTaches) > 0 or allDone:
        if len(sim.plt.listeTaches) <= nbTacheSim:
            while len(sim.plt.listeTaches) != nbTacheSim and len(sim.taches) > 0 :
                if len(sim.plt.listeTaches) >= 1:
                    t = rdm.choice(sim.taches)
                    sim.plt.listeTaches.append(t)
                    sim.taches.pop(sim.taches.index(t))
                
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

                allDone = True
                if ag.tacheToDo :
                    if ag.tacheToDo.enCours :
                        allDone = False

        # Update du screen, affichage du design de map, pause du programme
        mapS = sim.plt.itf.skins_map_update(sim.plt.canvas, mapS, skins)
        time.sleep(0.02)

        tour+=1
        print(tour)
        print(len(sim.taches) > 0)
        print(len(sim.plt.listeTaches) > 0)
        print(not(allDone))

    print("END")

    sim.plt.delcv()
    sim.plt.itf.gameFini(sim.layer.getWinner())
    sim.plt.start()
    return None


if __name__ == "__main__" :
    nbAgentE1, nbAgentE2, heuristiqueE1, heuristiqueE2, choixTacheE1, choixTacheE2, nbTaches, nbTacheSim = preMain()
    main(nbAgentE1, nbAgentE2, heuristiqueE1, heuristiqueE2, choixTacheE1, choixTacheE2, nbTaches, nbTacheSim)