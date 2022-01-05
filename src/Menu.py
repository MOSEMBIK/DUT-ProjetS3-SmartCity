from src.Interface import *

class Menu :
    def __init__(self):
        self.itf = Interface ('menu.png')

    def start(self) :
        self.itf.main_loop()