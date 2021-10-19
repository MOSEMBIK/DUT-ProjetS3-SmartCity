from src.Environnement import Environnement
from src.Case import *

Env = Environnement("Map")
for i in range(3):
    Env.init_rooms()
Env.main_loop()
