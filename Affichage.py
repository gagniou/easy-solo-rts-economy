import pygame
from random import *
from pygame.locals import *

from Ressource import*
from Unit import*
from Item import liste_Item
timer=0



def afficher_fond(fenetre):
    #affichage image fond
    pygame.draw.rect(fenetre,(43,160,70),(0,20,700,680),0)
    pygame.draw.rect(fenetre,(43,160,70),(700,20,700,680),0)
    pygame.draw.rect(fenetre,(60,60,60),(0,0,1400,20),0)
    
def afficher_ATH(fenetre):
    pygame.draw.rect(fenetre,(60,60,60),(0,500,400,200),0)
    pygame.draw.rect(fenetre,(60,60,60),(1000,500,400,200),0)
    
def afficher_texte(fenetre):
    global timer,font,font_s

    font=pygame.font.SysFont("comicsansms",18,bold=False,italic=False)
    font_s=pygame.font.SysFont("comicsansms",12,bold=False,italic=False)
    
    timer=timer+1
    text=font.render(str(timer),1,(255,255,0))
    fenetre.blit(text,(2,17))

    return

def afficher_image(fenetre):

    return 

def afficher_Item(fenetre,liste_Item):
    for i in liste_Item:
        if type(i)==Ressource:
            pygame.draw.rect(fenetre,i.couleurRGB,(i.centre_x-i.taille/2,i.centre_y-i.taille/2,i.taille,i.taille),0)
    for i in liste_Item:
        if type(i)!=Ressource:
            pygame.draw.rect(fenetre,i.couleurRGB,(i.centre_x-i.taille/2,i.centre_y-i.taille/2,i.taille,i.taille),0)

        #rect tant qu'on a pas des image
    return

def afficher_selection(fenetre,selection):
    if selection!=[]:
        if len(selection)==1:
            pygame.draw.rect(fenetre,(0,0,0),(20,520,60,60),0)
            #image dans cadre plus tard
            text_nom=font.render(selection[0].nom,1,(0,0,0))
            

            fenetre.blit(text_nom,(100,520))
            if type(selection[0])==Unit:
                text_hp=font.render(str(selection[0].hp),1,(0,0,0))
                text_carry=font.render(str(selection[0].carry),1,(0,0,0))
                text_res=font.render(selection[0].carryname,1,(0,0,0))
                fenetre.blit(text_hp,(100,535))
                fenetre.blit(text_carry,(100,555))
                fenetre.blit(text_res,(150,555))
            if type(selection[0])==Ressource:
                text_Qt=font.render(str(selection[0].Qt),1,(0,0,0))
                fenetre.blit(text_Qt,(100,555))
        else:
            text_nom=font.render("trop de selection",1,(0,0,0))
            fenetre.blit(text_nom,(100,520))

def afficher_ressources(fenetre,liste_ressource):
    text_food=font_s.render("food "+str(liste_ressource[0]),1,(0,0,0))
    text_wood=font_s.render("wood "+str(liste_ressource[1]),1,(0,0,0))
    text_gold=font_s.render("gold "+str(liste_ressource[3]),1,(0,0,0))
    text_stone=font_s.render("stone "+str(liste_ressource[2 ]),1,(0,0,0))

    fenetre.blit(text_food,(10,2))
    fenetre.blit(text_wood,(110,2))
    fenetre.blit(text_gold,(210,2))
    fenetre.blit(text_stone,(310,2))
    
