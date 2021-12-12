from src.Interface import *

class Layer:
    def __init__(self, interface):
        self.itf: Interface = interface
        self.frame1 = self.itf.addBoard(0)
        self.frame2 = self.itf.addBoard(2)
        self.itf.addText("Score", self.frame1)
        self.itf.addText("Score", self.frame2)
