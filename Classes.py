#-*-coding:UTF-8 -*
import os
import time
from random import randrange

import pygame
from pygame.display import *
from pygame.image import *
from pygame.locals import *

from constante_dk import *

pygame.init()


class Niveau:

    def generer(self,fichier_niveau):
        with open(fichier_niveau,"r") as fichier:
            fichier=fichier.read()

            self.structure_niveau=[]
            self.xa=0
            self.ya=0

            for elements in fichier:
                if elements=="m":
                    self.structure_niveau.append((self.xa,self.ya))


                if self.xa==450:
                    self.xa=0
                    self.ya+=30
                else:
                    self.xa+=30

    def afficher(self,position_perso,position_dk,position_ennemi,ennemis,position_ennemi_deux):
        fenetre.blit(fond,(0,0))
        fenetre.blit(depart,(0,0))
        fenetre.blit(arrivee,(420,420))

        for elements in self.structure_niveau:
            fenetre.blit(mur,(elements))

        fenetre.blit(position_dk,(position_perso))
        fenetre.blit(ennemis,(position_ennemi))
        fenetre.blit(ennemis,(position_ennemi_deux))

        flip()

class Perso:
    def __init__(self):
        self.x=0
        self.y=0

    def deplacer(self,direction,position_dk,structure_niveau):

        if direction=="droite":
            avancer=True
            if self.x != 420:
                for elements in structure_niveau:
                    if elements == (self.x+30,self.y):
                        avancer=False
                
                if avancer==True:
                    self.perso=load(position_dk).convert_alpha()
                    self.x+=30
        if direction=="gauche":
            avancer=True
            if self.x != 0:
                for elements in structure_niveau:
                    if elements == (self.x-30,self.y):
                        avancer=False

                if avancer==True:
                    self.perso=load(position_dk).convert_alpha()
                    self.x-=30
        if direction=="haut":
            avancer=True
            if self.y != 0:

                for elements in structure_niveau:
                    if elements == (self.x,self.y-30):
                        avancer=False
                
                if avancer==True:

                    self.perso=load(position_dk).convert_alpha()
                    self.y-=30
        if direction=="bas":
            avancer=True
            if self.y != 420:

                for elements in structure_niveau:
                    if elements == (self.x,self.y+30):
                        avancer=False
                
                if avancer==True:

                    self.perso=load(position_dk).convert_alpha()
                    self.y+=30

class Ennemi:
    def __init__(self):
        self.pouvoir_commencer_a_ne_pas_reculer=False
    def definir_mouvement_pour_lvl1(self,structure_niveau):
        self.quel_deplacement=["droite","gauche","haut","bas"]
        self.variable_pour_random=4
        self.repeter_pour_pas_depasser_bordures=True

        for elements in structure_niveau:
            if elements==(self.x,self.y-30):
                self.quel_deplacement.remove("haut")
                self.variable_pour_random-=1
            
            elif self.y==0:
                if self.repeter_pour_pas_depasser_bordures==True:
                    self.quel_deplacement.remove("haut")
                    self.variable_pour_random-=1

            if elements==(self.x,self.y+30):
                self.quel_deplacement.remove("bas")
                self.variable_pour_random-=1
            
            elif self.y==420:
                if self.repeter_pour_pas_depasser_bordures==True:
                    self.quel_deplacement.remove("bas")
                    self.variable_pour_random-=1


            if elements==(self.x+30,self.y):
                    self.quel_deplacement.remove("droite")
                    self.variable_pour_random-=1

            elif self.x==420:
                if self.repeter_pour_pas_depasser_bordures==True:
                    self.quel_deplacement.remove("droite")
                    self.variable_pour_random-=1


            if elements==(self.x-30,self.y):
                self.quel_deplacement.remove("gauche")
                self.variable_pour_random-=1

            elif self.x==0:
                if self.repeter_pour_pas_depasser_bordures==True:
                    self.quel_deplacement.remove("gauche")
                    self.variable_pour_random-=1

            self.repeter_pour_pas_depasser_bordures=False

        if self.pouvoir_commencer_a_ne_pas_reculer==True:

            if self.variable_pour_random!=1:

                if self.dou_il_vient=="haut":
                    if "bas" in self.quel_deplacement:
                        self.quel_deplacement.remove("bas")
                        self.variable_pour_random-=1

                elif self.dou_il_vient=="bas":
                    if "haut" in self.quel_deplacement:
                        self.quel_deplacement.remove("haut")
                        self.variable_pour_random-=1

                elif self.dou_il_vient=="droite":
                    if "gauche" in self.quel_deplacement:
                        self.quel_deplacement.remove("gauche")
                        self.variable_pour_random-=1

                elif self.dou_il_vient=="gauche":
                    if "droite" in self.quel_deplacement:
                        self.quel_deplacement.remove("droite")
                        self.variable_pour_random-=1

        self.quel_deplacement=self.quel_deplacement[randrange(self.variable_pour_random)]
        self.pouvoir_commencer_a_ne_pas_reculer=True
        self.dou_il_vient=str(self.quel_deplacement)

    def definir_mouvement_pour_lvl2(self,structure_niveau,absices_dk,ordonnées_dk):
        self.quel_deplacement=["droite","gauche","bas","haut"]
        self.direction_quil_faudrait_potentiellement_emprenter=[]
        self.elements_supprimés=0
        self.position_du_singe_x=self.x-absices_dk
        self.position_du_singe_y=self.y-ordonnées_dk
        
        for elements in structure_niveau:
            if elements==(self.x+30,self.y):
                self.quel_deplacement.remove("droite")
                self.elements_supprimés+=1
            elif self.x==420:
                if "droite" in self.quel_deplacement:
                    self.quel_deplacement.remove("droite")
                    self.elements_supprimés+=1
            
            if elements==(self.x-30,self.y):
                self.quel_deplacement.remove("gauche")
                self.elements_supprimés+=1
            elif self.x==0:
                if "gauche" in self.quel_deplacement:
                    self.quel_deplacement.remove("gauche")
                    self.elements_supprimés+=1
            
            if elements==(self.x,self.y-30):
                self.quel_deplacement.remove("haut")
                self.elements_supprimés+=1
            elif self.y==0:
                if "haut" in self.quel_deplacement:
                    self.quel_deplacement.remove("haut")
                    self.elements_supprimés+=1
            
            if elements==(self.x,self.y+30):
                self.quel_deplacement.remove("bas")
                self.elements_supprimés+=1
            elif self.y==420:
                if "bas" in self.quel_deplacement:
                    self.quel_deplacement.remove("bas")
                    self.elements_supprimés+=1

        if self.position_du_singe_x<0:
            if "gauche" in self.quel_deplacement:
                self.quel_deplacement.remove("gauche")
        elif self.position_du_singe_x>0:
            if "droite" in self.quel_deplacement:
                self.quel_deplacement.remove("droite")
            

        if self.position_du_singe_y>0:
            if "bas" in self.quel_deplacement:
                self.quel_deplacement.remove("bas")
        elif self.position_du_singe_y<0:
            if "haut" in self.quel_deplacement:
                self.quel_deplacement.remove("haut")

        

        if "haut" in self.quel_deplacement:
            if self.position_du_singe_x<=self.position_du_singe_y:
                self.quel_deplacement=["haut"]
            else:
                if "doite" in self.quel_deplacement:
                    self.quel_deplacement=["droite"]
                elif "gauche" in self.quel_deplacement:
                    self.quel_deplacement=["gauche"]

        

    def deplacer(self):
        if self.quel_deplacement=="haut":
            self.y-=1
        elif self.quel_deplacement=="bas":
            self.y+=1
        elif self.quel_deplacement=="droite":
            self.x+=1
        elif self.quel_deplacement=="gauche":
            self.x-=1