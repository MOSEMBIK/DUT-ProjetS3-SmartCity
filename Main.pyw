import time
from random import *
from src.Simulation import *
from src.Interface import *

from src.Plateau import *
from src.Case import *
from tkinter import *
from PIL import ImageTk, Image


def main():
    sim: Simulation = Simulation("SmartCity - MARS", 'img/logo/smartCorp.png', 2, "", 2)
    mapS = sim.plt.itf.skins_map_update(sim.plt.canvas, None, None)

    sim.allGoToRandom()

    allDone = False

    while len(sim.taches) > 0 or len(sim.plt.listeTaches) > 0 or allDone:
        if len(sim.plt.listeTaches) <= 4:
            for i in range(6):
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

                if ag.tacheToDo :
                    if ag.tacheToDo.enCours :
                        allDone = False
                    else :
                        allDone = True

        # Update du screen, affichage du design de map, pause du programme
        mapS = sim.plt.itf.skins_map_update(sim.plt.canvas, mapS, skins)
        # time.sleep(0.01)

    time.sleep(5)
    print("END")

    sim.plt.delcv()
    sim.plt.itf.gameFini(sim.layer.getWinner())
    sim.plt.start()
    return None


main()
