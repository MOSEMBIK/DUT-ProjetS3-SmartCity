import time
from random import *
from src.Simulation import *
from src.Interface import *

from src.Plateau import *
from src.Case import *


def main():
    sim: Simulation = Simulation("", 1, "", 1, 2, "Map")

    maxTour = 150
    sim.allGoToRandom()
    # del "#" to set trajet of agent1 to Case of coords = [46, 23]
    sim.agentGoTo(0,0, sim.plt.getCase(46, 23))
    #sim.agentGoTo(0,0, sim.plt.getCase(0, 0))
    agent1 = sim.equipe[0].agents[0]
    #agent2 = sim.equipe[0].agents[1]

    idCanva = sim.skin.get(agent1)
    #idCanva2 = sim.skin.get(agent2)


    print("Agent 1")
    print("Start : ", agent1.trajet[0].getCoords())
    print("Goal : ", agent1.trajet[-1].getCoords())
    print("Len Trajet : ", len(agent1.trajet))
    print()
    #print("Agent 2")
    #print("Start : ",agent2.trajet[0].getCoords())
    #print("Goal : ",agent2.trajet[-1].getCoords())
    #print("Len Trajet : ",len(agent2.trajet))
    #print()

    for i in range(maxTour):
        # print("Position : ",agent1.trajet[agent1.caseOfTrajet].getCoords())

        sim.allMove()
        for e in range(len(sim.equipe)):
            for a in sim.equipe[e].getAgents():
                ag = sim.equipe[e].getAgents()[a]
                Interface.imageMove(sim.plt.canvas, idCanva, ag.trajet[ag.caseOfTrajet].getCoords())
                sim.plt.canvas.update()
                #Interface.imageMove(sim.plt.canvas, idCanva2, ag.trajet[ag.caseOfTrajet].getCoords())
                #sim.plt.canvas.update()
                print("E :", sim.equipe[e].id, "A :", 1 + ag.id, ag.trajet[ag.caseOfTrajet].getCoords())
        time.sleep(0.1)

    sim.plt.start()
    return None


main()
