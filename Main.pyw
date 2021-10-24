import asyncio
import time

from src.Environnement import Environnement
from src.Case import *
from src.Lieu import Lieu


def main ():

    Env = Environnement("Map", 0)
    for i in (1, 5):
        Env.init_rooms(i)
    Env.main_loop()
    
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
