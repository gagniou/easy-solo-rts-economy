from random import randint

from Item import liste_Item
from Ressource import *
from Batiment import *

class Unit(Item):
                # civil 1/0
    def __init__(self,x,y,taille,couleur,hp,civil,nom=''):

        self.hp=hp
        self.speed=10
        if (civil==1):
            self.nom='villageois'
            self.work=4
            self.carry=0
            self.carryname=''
            self.carrytype=-1
            self.carry_limite=10
            self.target=-1
            self._working=0
            self.dest=(x,y)
            self.state=0
            self.workplace='null'
            
        Item.__init__(self,x,y,taille,couleur)

    def working(self,liste_ressource):
        if self.state==0:
            for i in liste_Item:
                if i.centre_y-i.taille/2<self.centre_y<i.centre_y+i.taille/2:
                    if i.centre_x-i.taille/2<self.centre_x<i.centre_x+i.taille/2:
                        if type(i)==Ressource:
                            if self.carry!=0:
                                if i.type!=self.carrytype:
                                    self.carry=0
                            self._working=0
                            self.state=1
                            self.workplace=i
                            self.carryname=i.nom
                            self.carrytype=i.type
                            self.target=i
                        if type(i)==Batiment:
                                if self.carry>0:
                                    if i.deposit==-1 or i.deposit==self.carrytype:
                                        self.deposit(liste_ressource)
                                
        elif self.state==1:
            if self.workplace=='null':
                self.state=0
                self.dest=(self.centre_x,self.centre_y)
            else:
                if self.workplace.centre_x-self.workplace.taille/2<self.centre_x<self.workplace.centre_x+self.workplace.taille/2:
                    if self.workplace.centre_x-self.workplace.taille/2<self.centre_x<self.workplace.centre_x+self.workplace.taille/2:
                        if self.carry<self.carry_limite:
                            if self._working==0:
                                self._working=self.target.dur
                            elif self._working>0:
                                self._working-=self.work
                            else:
                                if  self.workplace.Qt>0:
                                    self._working=0
                                    self.carry+=1
                                    self.workplace.Qt-=1
                                    if self.workplace.Qt==0:
                                        liste_Item.remove(self.workplace)
                                        self.chomage()
                        if self.carry==self.carry_limite:
                            self.state=2 # deposit
                            depot=[]
                            for i in liste_Item:
                                if type(i)==Batiment:
                                    depot.append(i)
                                    #techniquemnt il faudrai une recherche du point le plus proche
                                    self.dest=(depot[0].centre_x,depot[0].centre_y+20)
                    else:
                        self.chomage()
                        self.state=0;
                else:
                    self.chomage()
                    self.state=0;
                            
        elif self.state==2:
                self.deposit(liste_ressource)
                if self.workplace!='null':
                    self.dest=(self.workplace.centre_x,self.workplace.centre_y)

    def chomage(self):
        self.workplace='null'
        self.carryname=""
        self.dest=(self.centre_x,self.centre_y)
        if self.carry==0:
            self.carrytype==-1
        
        
    def deposit(self,liste_ressource):
        liste_ressource[self.carrytype]+=self.carry
        self.carry=0
        self.state=0

    def move(self,liste_ressource):
        global liste_Item
        x=self.centre_x-self.dest[0]
        y=self.centre_y-self.dest[1]
        if x!=0 and y!=0: 
            move_x=abs(x)/(abs(x)+abs(y))*self.speed
            move_y=abs(y)/(abs(x)+abs(y))*self.speed
            if x>0:
                move_x*=-1
            if y>0:
                move_y*=-1
            if abs(x)>4:
                self.centre_x+=move_x
            if abs(y)>4:
                self.centre_y+=move_y
            if abs(x)<5 and abs(y)<5:
                self.working(liste_ressource)
                                        
