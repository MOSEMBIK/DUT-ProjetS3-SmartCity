import asyncio
import math

from src.Environnement import Environnement
from src.Case import *
import src.Lieu

Env = Environnement("Map")
for i in range(3):
    Env.init_rooms(i)
print(Env.getContenu()[2].getLocation())
Env.main_loop()

