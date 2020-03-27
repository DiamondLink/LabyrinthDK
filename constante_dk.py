#-*-coding:UTF-8 -*
import os
import time
import pygame
from random import randrange
from tkinter import *
from pygame.image import *
from pygame.display import *
from pygame.locals import *
pygame.init()

fenetre_tkinter=Tk()
label_tkinter=Label(fenetre_tkinter,text="Voulez vous continuer en mode plein écran ?")
bouton_tkinter=Button(fenetre_tkinter,text="Continuer",command=fenetre_tkinter.destroy)
variable_tkinter=StringVar()
oui_tkinter=Radiobutton(fenetre_tkinter,text="oui",variable=variable_tkinter,value="oui")   
non_tkinter=Radiobutton(fenetre_tkinter,text="non",variable=variable_tkinter,value="non")
label_tkinter.grid(padx=20,pady=20)
oui_tkinter.grid(padx=20,pady=20)
non_tkinter.grid(padx=20,pady=20)
bouton_tkinter.grid(padx=50,pady=50)
oui_tkinter.select()
non_tkinter.select()
fenetre_tkinter.mainloop()
variable_tkinter=variable_tkinter.get()

if variable_tkinter=="oui":
    fenetre=set_mode((450,450),FULLSCREEN)
else:
    fenetre=set_mode((450,450))

acceuil=load("sprites//accueil.png").convert()
dk_bas=load("sprites//dk_bas.png").convert_alpha()
dk_haut=load("sprites//dk_haut.png").convert_alpha()
dk_gauche=load("sprites//dk_gauche.png").convert_alpha()
dk_droite=load("sprites//dk_droite.png").convert_alpha()
fond=load("sprites//fond.png").convert()
arrivee=load("sprites//arrivee.png").convert_alpha()
mur=load("sprites//mur.png").convert()
depart=load("sprites//depart.png").convert_alpha()
icone=load("sprites//icone.ico").convert_alpha()
victoire=load("sprites//victoire.png").convert()
ennemis=load("sprites//goomba.png").convert_alpha()

set_icon(icone)
set_caption("Le Labyrinth")
fenetre.blit(acceuil,(0,0))

continuer=True
changer_niveau=True
pouvoir_bouger=False

flip()


