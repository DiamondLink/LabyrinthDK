#-*-coding:UTF-8 -*
import os
import time
import pygame
from random import randrange
from pygame.image import *
from pygame.display import *
from pygame.locals import *
pygame.init()

from constante_dk import *
from Classes import *

niveau=Niveau()
personnage=Perso()
ennemit=Ennemi()
ennemid=Ennemi()
ennemid.x=0
ennemid.y=420
ennemit.x=420
ennemit.y=420
ennemit.quel_deplacement="gauche"
ennemid.quel_deplacement="droite"

perdu=load("sprites//level_failed.png").convert()
personnage.perso=load("sprites//dk_bas.png").convert_alpha()
pouvoir_changer_direction_ennemi=0
pour_regler_le_bug_de_façon_je_sais_pas_comment_faire=True
changer_niveau=True
while continuer:


    if personnage.x==420 and personnage.y==420:
        fenetre.blit(victoire,(0,0))
        changer_niveau=False
        pouvoir_bouger=False
        flip()

    if (personnage.x==ennemit.x and personnage.y==ennemit.y) or (personnage.x==ennemid.x and personnage.y==ennemid.y):
        fenetre.blit(perdu,(0,0))
        changer_niveau=False
        pouvoir_bouger=False
        ennemid.dou_il_vient=[]
        ennemit.dou_il_vient=[]
        pour_regler_le_bug_de_façon_je_sais_pas_comment_faire=True
        flip()

    if pouvoir_bouger==True:
        if pouvoir_changer_direction_ennemi==30:
            pouvoir_changer_direction_ennemi=0
            if choix_du_niveau==1:
                ennemit.definir_mouvement_pour_lvl1(niveau.structure_niveau)
                ennemid.definir_mouvement_pour_lvl1(niveau.structure_niveau)
            elif choix_du_niveau==2:
                ennemit.definir_mouvement_pour_lvl2(niveau.structure_niveau,personnage.x,personnage.y)
                ennemid.definir_mouvement_pour_lvl2(niveau.structure_niveau,personnage.x,personnage.y)

            if pour_regler_le_bug_de_façon_je_sais_pas_comment_faire==True:
                ennemid.quel_deplacement="droite"
                ennemid.dou_il_vient="droite"
                ennemit.quel_deplacement="gauche"
                ennemit.dou_il_vient="gauche"
                pour_regler_le_bug_de_façon_je_sais_pas_comment_faire=False
                
        else:
            pygame.time.Clock().tick(110)
            pouvoir_changer_direction_ennemi+=1
            ennemit.deplacer()
            ennemid.deplacer()
            niveau.afficher((personnage.x,personnage.y),personnage.perso,(ennemit.x,ennemit.y),ennemis,(ennemid.x,ennemid.y))

    for evenements in pygame.event.get():
        if evenements.type==QUIT:
            continuer=False

        if evenements.type==KEYDOWN:

            if evenements.key==K_F11:
                pour_regler_le_bug_de_façon_je_sais_pas_comment_faire=True
                ennemid.pouvoir_commencer_a_ne_pas_reculer=False
                ennemit.pouvoir_commencer_a_ne_pas_reculer=False
                fenetre.blit(acceuil,(0,0))
                changer_niveau=True
                pouvoir_bouger=False
                personnage.x=0
                personnage.y=0
                ennemid.quel_deplacement=[]
                ennemit.quel_deplacement=[]
                ennemid.dou_il_vient=[]
                ennemit.dou_il_vient=[]
                pour_regler_le_bug_de_façon_je_sais_pas_comment_faire=True
                pouvoir_changer_direction_ennemi=0
                ennemit.x=420
                ennemit.y=420
                ennemid.x=0
                ennemid.y=420
                
                flip()

            if evenements.key==K_F12:
                continuer=False

            if evenements.key==K_F1:
                ennemid.quel_deplacement=[]
                ennemit.quel_deplacement=[]
                ennemid.dou_il_vient=[]
                ennemit.dou_il_vient=[]
                choix_du_niveau=1
                ennemit.pouvoir_commencer_a_ne_pas_reculer=False
                ennemid.pouvoir_commencer_a_ne_pas_reculer=False
                personnage.x=0
                personnage.y=0
                pouvoir_changer_direction_ennemi=0
                ennemit.x=420
                ennemit.y=420
                ennemid.x=0
                ennemid.y=420
                pouvoir_bouger=True
                if changer_niveau==True:
                    niveau.generer("sprites//Obstacles labyrinthe lvl.1.txt")
                    niveau.afficher((personnage.x,personnage.y),dk_bas,(ennemit.x,ennemit.y),ennemis,(ennemid.x,ennemid.y))
                    changer_niveau=False

            if evenements.key==K_F2:
                ennemid.quel_deplacement=[]
                ennemit.quel_deplacement=[]
                ennemid.dou_il_vient=[]
                ennemit.dou_il_vient=[]
                choix_du_niveau=2
                ennemit.pouvoir_commencer_a_ne_pas_reculer=False
                ennemid.pouvoir_commencer_a_ne_pas_reculer=False
                personnage.x=0
                personnage.y=0
                pouvoir_changer_direction_ennemi=0
                ennemit.x=420
                ennemit.y=420
                ennemid.x=0
                ennemid.y=420
                pouvoir_bouger=True
                if changer_niveau==True:
                    niveau.generer("sprites//Obstacles labyrinthe lvl.2.txt")
                    niveau.afficher((personnage.x,personnage.y),dk_bas,(ennemit.x,ennemit.y),ennemis,(ennemid.x,ennemid.y))
                    changer_niveau=False


            if evenements.key==K_RIGHT:
                if pouvoir_bouger==True:
                    personnage.deplacer("droite","sprites//dk_droite.png",niveau.structure_niveau)
                    niveau.afficher((personnage.x,personnage.y),personnage.perso,(ennemit.x,ennemit.y),ennemis,(ennemid.x,ennemid.y))

            if evenements.key==K_LEFT:
                if pouvoir_bouger==True:
                    personnage.deplacer("gauche","sprites//dk_gauche.png",niveau.structure_niveau)
                    niveau.afficher((personnage.x,personnage.y),personnage.perso,(ennemit.x,ennemit.y),ennemis,(ennemid.x,ennemid.y))

            if evenements.key==K_UP:
                if pouvoir_bouger==True:
                    personnage.deplacer("haut","sprites//dk_haut.png",niveau.structure_niveau)
                    niveau.afficher((personnage.x,personnage.y),personnage.perso,(ennemit.x,ennemit.y),ennemis,(ennemid.x,ennemid.y))

            if evenements.key==K_DOWN:
                if pouvoir_bouger==True:
                    personnage.deplacer("bas","sprites//dk_bas.png",niveau.structure_niveau)
                    niveau.afficher((personnage.x,personnage.y),personnage.perso,(ennemit.x,ennemit.y),ennemis,(ennemid.x,ennemid.y))