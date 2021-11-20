import asyncio
import time

from src.Simulation import *

from src.Plateau import *
from src.Case import *


def main():

    env = Plateau("Map")
    env.test_image()
    #env.deplacement()
    case = env.getCase(23, 36)
    env.nearRoads(case)


    env.main_loop()

    global tour
    global lastTour
    tour = 0
    lastTour = 0

    maxTour = 20
    for i in range(maxTour):
        # Corps réel
        # Création des taches, deplacements des agents, ...


        # Passage au tour suivant
        time.sleep(5)
        lastTour = tour
        tour+=1
    return None

main()
