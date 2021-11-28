import time
from random import *
from src.Simulation import *
from src.Interface import *

from src.Plateau import *
from src.Case import *


def main():
    sim: Simulation = Simulation("SmartCity - MARS", 'img/logo/smartCorp.ico',  1, "", 2, 2)
    maxTour = 1000

    sim.allGoToRandom()
    # del "#" to set trajet of agent1 to Case of coords
    sim.agentGoTo(0,0, sim.plt.getCase(36, 20))
    #sim.agentGoTo(0,0, sim.plt.getCase(0, 0))
    agent1 : Agent = sim.equipe[0].agents[0]
    agent2 : Agent = sim.equipe[0].agents[1]

    #idCanva = sim.skin.get(agent1)
    #idCanva2 = sim.skin.get(agent2)


    print("Agent 1")
    print("Start : ", agent1.trajet[0].getCoords())
    print("Goal : ", agent1.trajet[-1].getCoords())
    print("Len Trajet : ", len(agent1.trajet))
    print()
    print("Agent 2")
    print("Start : ",agent2.trajet[0].getCoords())
    print("Goal : ",agent2.trajet[-1].getCoords())
    print("Len Trajet : ",len(agent2.trajet))
    print()

    mapS = sim.plt.itf.skins_map_update(sim.plt.canvas, None, None)
    for i in range(maxTour):
        skins = []
        # print("Position : ",agent1.trajet[agent1.caseOfTrajet].getCoords())

        print()
        print("Tour ", i)

        if len(agent1.trajet) > 1 :
            sim.allMove()
            for e in range(len(sim.equipe)):
                for a in sim.equipe[e].getAgents():
                    ag : Agent = sim.equipe[e].getAgents()[a]

                    print("Agent ", ag.id)
                    print("Trajet : ", len(ag.trajet)-1, "Case : ", ag.caseOfTrajet)
                    print("Charge : ", ag.charge)

                    Interface.imageMove(sim.plt.canvas, sim.skin.get(ag), ag.trajet[ag.caseOfTrajet].getCoords())
                    skins.append(sim.skin.get(ag))
                    #sim.plt.itf.moveSkin(sim.skin.get(ag), ag.trajet[ag.caseOfTrajet].getCoords())
                    #print("E :", sim.equipe[e].id, "A :", 1 + ag.id, ag.trajet[ag.caseOfTrajet].getCoords())
            
            # Update du screen, affichage du design de map, pause du programme
            mapS = sim.plt.itf.skins_map_update(sim.plt.canvas, mapS, skins)
            #time.sleep(0.02)
            
        else :
            sim.allGoToRandom()

    sim.plt.start()
    return None

main()
