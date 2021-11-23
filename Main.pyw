import asyncio
import time
from random import *
from src.Simulation import *

from src.Plateau import *
from src.Case import *


def main():
    sim = Simulation("", 1, "", 1, 1, "Map")
    sim.plt.test_image()

    sim.plt.start()

    maxTour = 150
    sim.allGoToRandom()
    print(sim.equipe[0].getAgents()[0].trajet[sim.equipe[0].getAgents()[0].caseOfTrajet].getCoords())
    sim.agentGoTo(0,0, sim.plt.getCase(46,23))
    for i in range(maxTour):
        sim.allMove()
        for e in range(len(sim.equipe)):
            for a in sim.equipe[e].getAgents() :
                ag = sim.equipe[e].getAgents()[a]
                if ag.id == 0 :
                    print(sim.equipe[e].id, ag.id, ag.trajet[ag.caseOfTrajet].getCoords())

    return None


main()
