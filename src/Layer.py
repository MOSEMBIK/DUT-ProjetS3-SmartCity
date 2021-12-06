from src.Interface import *


class Layer:
    def __init__(self, interface):
        self.itf: Interface = interface

        self.itf.addText('AAAAAAAAAAAAAA', 10, 10)

        #self.itf.addTexte('AAAAAAAAAAAAAA', 10, 10)

