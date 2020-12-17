
from Item import liste_Item
from Ressource import *

class Batiment(Item):
    def __init__(self,x,y,taille,couleur,ID):
        Item.__init__(self,x,y,taille,couleur)
        if ID==0:
            self.nom="forum"
            self.hp=200
            #deposit = -1= all / else ressource spécifique
            self.deposit=-1
