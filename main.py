import pygame
from random import *
from pygame.locals import *

from Item import liste_Item
from Affichage import*

from Unit import*
from Batiment import*
from Ressource import*
###############################################################################################################################################
timer=0 #print nb_frame

continuer=1 # boucle simulation
fps=30


joueurcouleur=(180,0,0)
###############################################################################################################################################

def init():
    global liste_Item
    liste_Item.append(Batiment(200,200,40,joueurcouleur,0))
    liste_Item.append(Unit(230,180,15,joueurcouleur,30,1))
    liste_Item.append(Unit(230,200,15,joueurcouleur,30,1))
    liste_Item.append(Unit(230,220,15,joueurcouleur,30,1))

    for i in range(25):
        ressource=Ressource("",0,randint(5,1395),randint(25,695),0,(0,0,0))
        x=randint(0,5)
        if x==0:
            ressource.nouriture_mouton()
        elif x==1:
            ressource.nouriture_baie()
        elif x==2:
            ressource.nouriture_ferme()
        elif x==3:
            ressource.pierre_mine()
        elif x==4:
            ressource.bois_foret()
        elif x==5:
            ressource.or_mine()
        liste_Item.append(ressource)
###############################################################################################################################################
        
def main():
    global timer,font,font_s
    pygame.init()
    fenetre = pygame.display.set_mode((1400, 700))
    pygame.display.set_caption("Simulateur")
    
    timer=0
    continuer=1
    
    
    liste_ressource=[0,0,0,0]
    
    nbcycle=0
    cycle_fin=1
    
    clock=pygame.time.Clock()
    selection=[]

    init()
    while continuer:
        got=0
        for event in pygame.event.get():
            if event.type==QUIT:
                continuer=0
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    continuer=0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    selection=[]
                    for i in liste_Item:
                        if type(i)==Unit or type(i)==Ressource:
                            if i.centre_y-i.taille/2<event.pos[1]<i.centre_y+i.taille/2:
                                if i.centre_x-i.taille/2<event.pos[0]<i.centre_x+i.taille/2:
                                    if got==0:
                                        selection.append(i)
                                        got+=1
                    if got==0:
                        selection=[]
                if event.button == 3:
                    if len(selection)==1:
                        if type(selection[0])==Unit:
                            if event.pos[1]>20:
                                if event.pos[1]>500:
                                    if 400<event.pos[0]<1000:
                                        selection[0].dest=(event.pos[0],event.pos[1])
                                else:
                                    selection[0].dest=(event.pos[0],event.pos[1])


        for i in liste_Item:
            if type(i)==Unit:
                i.move(liste_ressource)
        afficher_fond(fenetre)
        
        afficher_texte(fenetre)

        afficher_ressources(fenetre,liste_ressource)
        
        afficher_Item(fenetre,liste_Item)
        afficher_ATH(fenetre)
        afficher_selection(fenetre,selection)
        
        afficher_image(fenetre)

        clock.tick(fps)
        pygame.display.update()

    pygame.quit()



main()
