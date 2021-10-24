import asyncio
import time

from src.Environnement import Environnement
from src.Case import *
from src.Lieu import Lieu


def main ():

    Env = Environnement("Map", 600)

    idLieu = 0
    while idLieu < 2:
        if Env.init_rooms(idLieu):
            idLieu += 1
    Env.test_image()
    #Env.connect_rooms()
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
