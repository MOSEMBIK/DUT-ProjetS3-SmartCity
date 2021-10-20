import asyncio
import math

from src.Environnement import Environnement
from src.Case import *
from src.Lieu import Lieu

Env = Environnement("Map", 0)
for i in range(3):
    Env.init_rooms(i)
print(Env.getContenu()[2].getLocation())
Env.main_loop()

