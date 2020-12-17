from Item import*


#type = 0 nouriture | 1 bois | 2 pierre | 3 or | 4 fer
class Ressource(Item):
    def __init__(self,nom,dur,x,y,taille,couleur):
        self.nom=""
        self.dur=0 #durabilite/tps de collecte
        self.Qt=100 #quantité
        self.type=-1
        Item.__init__(self,x,y,taille,couleur)
        

    def nouriture_mouton(self):
        self.dur=5.001
        self.Qt=100
        self.nom="mouton"
        self.type=0
        self.couleurRGB=(240,240,240)
        self.taille=7
        
    def nouriture_baie(self):
        self.dur=10.001
        self.Qt=250
        self.nom="baie"
        self.type=0
        self.couleurRGB=(200,200,100)
        self.taille=12

    def nouriture_ferme(self):
        self.dur=15.001
        self.Qt=800
        self.nom="ferme"
        self.type=0
        self.couleurRGB=(150,200,0)
        self.taille=25




    def pierre_mine(self):
        self.dur=25.001
        self.Qt=450
        self.nom="pierre"
        self.type=2
        self.couleurRGB=(175,175,175)
        self.taille=15

    def or_mine(self):
        self.dur=20.001
        self.Qt=450
        self.nom="Or"
        self.type=3
        self.couleurRGB=(175,175,0)  
        self.taille=18
        
    def bois_foret(self):
        self.dur=10.001
        self.Qt=120
        self.nom="arbre"
        self.type=1
        self.couleurRGB=(30,175,30)
        self.taille=12
