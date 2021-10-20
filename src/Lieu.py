import asyncio
import math

class Lieu:

    def __init__(self, idLieu, nom):
        self.idLieu = idLieu
        self.nom = nom
        # Array avec les coordonnés de chaque case du lieu
        self.location = []

    # J'en ai besoin dans environnement
    def getLocation(self):
        return self.location
    # J'en ai aussi besoin dans environnement
    def setLocation(self, coord_array):
        self.location = coord_array

    # J'en ai toujours aussi besoin dans environnement
    def getIdLieu(self):
        return self.idLieu