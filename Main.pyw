import asyncio
import time


from src.Environnement import Environnement
from src.Case import *
from src.Lieu import Lieu


def main():

    env = Environnement("Map")
    env.test_image()
    env.deplacement()
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
