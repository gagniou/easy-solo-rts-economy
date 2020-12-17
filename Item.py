from math import sqrt

liste_Item=[]

class Item():
    def __init__(self,x,y,taille,couleur):
        self.centre_x=x
        self.centre_y=y
        
        self.taille=taille

        self.couleurRGB=couleur

    def dist(self,other):
        return sqrt((self.centre_x-other.centre_x)*(self.centre_x-other.centre_x)+(self.centre_y-other.centre_y)*(self.centre_y-other.centre_y))

