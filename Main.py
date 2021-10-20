import asyncio
import math

from src.Environnement import Environnement
from src.Case import *
from src.Lieu import Lieu

Env = Environnement("Map", 0)
for i in range(2):
    Env.init_rooms(2)
Env.main_loop()

