from src.Environnement import Environnement
from src.Case import *
from src.Lieu import Lieu


def main ():

    Env = Environnement("Map", 0)
    for i in (1, 5):
        Env.init_rooms(i)
    Env.main_loop()

    return None

main()
