import time
from random import *
from src.Simulation import *
from src.Interface import *

from src.Plateau import *
from src.Case import *


def main():
    sim: Simulation = Simulation("SmartCity - MARS", 'img/logo/smartCorp.png', 2, "", 5)
    mapS = sim.plt.itf.skins_map_update(sim.plt.canvas, None, None)
    maxTour = 10000

    sim.allGoToRandom()
    # del "#" to set trajet of agent1 to Case of coords
    # sim.agentGoTo(0, 0, sim.plt.getCase(36, 20))
    # sim.agentGoTo(0,0, sim.plt.getCase(0, 0))
    agent1: Agent = sim.equipe[0].agents['00']
    # agent2: Agent = sim.equipe[0].agents[1]

    # idCanva = sim.skin.get(agent1)
    # idCanva2 = sim.skin.get(agent2)

    # print("Agent 1")
    # print("Start : ", agent1.trajet[0].getCoords())
    # print("Goal : ", agent1.trajet[-1].getCoords())
    # print("Len Trajet : ", len(agent1.trajet))
    # print()
    # print("Agent 2")
    # print("Start : ", agent2.trajet[0].getCoords())
    # print("Goal : ", agent2.trajet[-1].getCoords())
    # print("Len Trajet : ", len(agent2.trajet))
    # print()

    while len(sim.plt.listeTaches) > 0:
        skins = []
        # print("Position : ",agent1.trajet[agent1.caseOfTrajet].getCoords())

        # print()
        # print("Tour ", i)

        if len(agent1.trajet) > 0:
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

            # Update du screen, affichage du design de map, pause du programme
            mapS = sim.plt.itf.skins_map_update(sim.plt.canvas, mapS, skins)
            # time.sleep(0.01)

        else:
            sim.allGoToRandom()

    print("END")

    sim.plt.start()
    return None


main()
