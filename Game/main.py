#!/usr/bin/python3
#-*- coding:Utf-8 -*-

#=== Import des modules 
from cProfile import run
import pygame
from pygame.locals import *
from random import *
from database import *
import yaml
from operator import itemgetter
from time import *

#Démarrage du jeu / Menu de chargement

class TextProgress:
    def __init__(self, font, message, color, bgcolor):
        self.font = font
        self.message = message
        self.color = color
        self.bgcolor = bgcolor
        self.offcolor = [c^40 for c in color]
        self.notcolor = [c^0xFF for c in color]
        self.text = font.render(message, 0, (255,0,0), self.notcolor)
        self.text.set_colorkey(1)
        self.outline = self.textHollow(font, message, color)
        self.bar = pygame.Surface(self.text.get_size())
        self.bar.fill(self.offcolor)
        width, height = self.text.get_size()
        stripe = Rect(0, height/2, width, height/4)
        self.bar.fill(color, stripe)
        self.ratio = width / 100.0

    def textHollow(self, font, message, fontcolor):
        base = font.render(message, 0, fontcolor, self.notcolor)
        size = base.get_width() + 2, base.get_height() + 2
        img = pygame.Surface(size, 16)
        img.fill(self.notcolor)
        base.set_colorkey(0)
        img.blit(base, (0, 0))
        img.blit(base, (2, 0))
        img.blit(base, (0, 2))
        img.blit(base, (2, 2))
        base.set_colorkey(0)
        base.set_palette_at(1, self.notcolor)
        img.blit(base, (1, 1))
        img.set_colorkey(self.notcolor)
        return img

    def render(self, percent=50):
        surf = pygame.Surface(self.text.get_size())
        if percent < 100:
            surf.fill(self.bgcolor)
            surf.blit(self.bar, (0,0), (0, 0, percent*self.ratio, 100))
        else:
            surf.fill(self.color)
            global finished
            finished = 1
        surf.blit(self.text, (0,0))
        #surf.blit(self.outline, (-1,-1))
        surf.set_colorkey(self.notcolor)
        return surf



entry_info = '/////////////////////////'
icon = pygame.image.load('Game/data/logo.png')
load = pygame.image.load('Game/data/titre1.png')
ch = 0

#this code will display our work, if the script is run...
if __name__ == '__main__':
    import random
    pygame.init()
    pygame.display.set_caption("Simon - Py")
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_icon(icon)
    screen.blit(load, (10, 0))

    #create our fancy text renderer
    font = pygame.font.Font(None, 60)
    font2 = pygame.font.SysFont('Comic Sans MS,Arial', 24)
    font3 = pygame.font.SysFont(None,22)
    white = 0, 225, 0
    renderer = TextProgress(font, entry_info, white, (40, 40, 40))
    text = renderer.render(0)

    #create a window the correct size
    
    screen.blit(text, (115, 330))
    bar1 = font.render(' ____________ ', True, (255,255,255))
    bar2 = font.render('|____________|', True, (255,255,255))
    author = font2.render('Chargement..', True, (255,255,255))
    screen.blit(author, (180,280))
    screen.blit(bar1, (105,290))
    screen.blit(bar2, (105,330))
    
    pygame.display.flip()

    progress = 1

    #wait for the finish
    finished = 0
    while not finished:
        dly = randint(160,640)
        pygame.time.delay(120)
        ch += 1
        for event in pygame.event.get():
            if event.type in (QUIT,KEYDOWN,MOUSEBUTTONDOWN):
                finished = 1
        
        progress = (progress + random.randint(0,3)) % 120
        text = renderer.render(progress)
        screen.blit(text, (115, 330))
        if ch == 2:
            donn1 = font3.render('Chargement des données..', True, (200,200,200))
            screen.blit(donn1,(115,390))
        if ch == 13:
            donn2 = font3.render('Chargement des données.. Ok', True, (200,200,200))
            screen.blit(donn2,(115,390))
        if ch == 17:
            data1 = font3.render('Chargement des datas..', True, (200,200,200))
            screen.blit(data1,(115,410))
        if ch == 33:
            data2 = font3.render('Chargement des datas.. Ok', True, (200,200,200))
            screen.blit(data2,(115,410))
        if ch == 39:
            db1 = font3.render('Chargement de la DataBase..', True, (200,200,200))
            screen.blit(db1,(115,430))
        if ch == 54:
            db2 = font3.render('Chargement de la DataBase.. Ok', True, (200,200,200))
            screen.blit(db2,(115,430))
        pygame.display.flip()


print("_______________________________________")
print("                                       ")
print(" Simon-Py vous souhaite la bienvenue ! ")
print("_______________________________________")
print("                                       ")

#================================================================================================================= Ressources

#=== liste des couleur utilisé , rangé suivant cet ordre ---> vert,rouge,bleu,jaune
couleur_sombre = [(0,90,0), (155,0,0), (0,55,125), (160,150,0)]
couleur_clair = [(0,225,0), (243,0,0), (0,205,255), (255,255,0)]
blanc, noir, rouge, bleu, jaune, vert, rose, argent, bronze, orange = (255,255,255), (0,0,0), (225,0,0), (0,15,255), (255,185,0), (0,195,25), (195,0,115), (170,170,170), (196, 156, 72), (230,65,0)

#=== liste de la position des couleurs sous la forme ((coin_haut_gauche_x,coin_haut_gauche_y),(largeur,hauteur))
#=== Ordre de rangement identique a la liste de couleur--> vert,rouge,bleu,jaune

#liste_pos = [((15,15),(225,225)) , ((260,15),(225,225)) , ((15,260),(225,225)) ,  ((260,260),(225,225))]
liste_pos = [((15,140),(140,225)) , ((140,15),(225,140)) , ((140,350),(225,135)) ,  ((350,140),(135,225))]
#Vert/Rouge/Bleu/Jaune
#=== Images
centre , fond , titre, help ,titre1= 'Game/data/none.png' , 'Game/data/fond3.png' , 'Game/data/titre.png', 'Game/data/aide.png','Game/data/titre1.png'

#==== Sons
son1 = pygame.mixer.Sound("Game/data/son1.wav")
son2 = pygame.mixer.Sound("Game/data/son2.wav")
son3 = pygame.mixer.Sound("Game/data/son3.wav")
son4 = pygame.mixer.Sound("Game/data/son4.wav")
liste_son = [son1, son2, son3, son4]

global defi
defi = 0

global rundefi
rundefi = 0
 
#======================================================================================================= Classes et fonctions 

def Image(image):
    '''____Fonction de chargement d'image___
       - nom de l'image
       - attribut alpha : Bool
    '''
                                           
    x =pygame.image.load(image).convert_alpha()
    return x
    
class Draw_rect :
    '''______Création de rectange(s)______
       - 2 méthodes possibles : 
             1 - gen -> dessine 1 carré 
                     - couleur
                     - position
             2 - gen_bg -> dessine les 4 carrés formant le fond
    '''
    def __init__(self):
        pass
    
    def gen(self,couleur,position):
        x = pygame.draw.rect(screen, couleur, Rect(position))
        return x
                                                 
    def gen_bg(self):
        n = 0
        while n != len(couleur_sombre):
            x = pygame.draw.rect(screen, couleur_sombre[n], Rect(liste_pos[n]))
            n += 1

class Texte :
    '''______Afficher un texte_____
       les attributs : 
       - texte 
       - taille de la font 
       - couleur - position
       @ -la police sera celle par défaut , sa suffira bien ^^
    '''
    def __init__(self, texte, taille, couleur, position):
        self.texte = texte
        self.taille = taille
        self.couleur = couleur
        self.position = position
        
        
    def affiche (self):    
        
        font = pygame.font.Font(None, self.taille)
        text = font.render(self.texte, 1, self.couleur) 
        text_pos = text.get_rect()
        text_pos.center = (self.position)

        screen.blit(text, text_pos)

        
        
class Sequence :
    '''_______Génère séquence________
       info : "seq" = séquence
    '''
    def __init__(self):
        self.level = 1
        self.seqordi = ''
        self.seq_player = ''
    
    def gen_seq(self):
        n = 0
        self.seqordi = ''
        while n != self.level :        
            x = randrange(4)
            self.seqordi += str(x)
            n += 1    
        return self.seqordi
        
    def change_level(self,win):
        if win == 1:
            self.level += 1
            print("[Logs] > L'ordinateur génère une séquence..")
        if win == 0:   
            global name
            print("[Logs] > Defi ", defi)
            print("[Logs] > self.level ", self.level)
            BLUE = (40, 120, 230)
            GREEN = (40, 230, 120)
            RED = (225,0,0)
            
            pygame.init()
            screen = pygame.display.set_mode((640, 480))
            center_x, center_y = 320, 240
            
            clock = pygame.time.Clock()
            font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
            lose = pygame.font.SysFont('Comic Sans MS,Arial', 36)
            title = lose.render('Loserrrr !', True, RED)
            title_rect = title.get_rect(center=(center_x, 175))
            prompt = font.render('Entrez vôtre pseudo :', True, BLUE)
            prompt_rect = prompt.get_rect(center=(center_x, center_y))
            
            name = ""
            user_input = font.render(name, True, GREEN)
            user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
            
            continuer = True
            
            while continuer:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        continuer = False
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                            continuer = False
                            break
                        elif event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                        else:
                            name += event.unicode
                        user_input = font.render(name, True, GREEN)
                        user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
            
                clock.tick(30)
            
                screen.fill(0)
                screen.blit(title, title_rect)
                screen.blit(prompt, prompt_rect)
                screen.blit(user_input, user_input_rect)
                pygame.display.flip()
            
            print("[Logs] (Pseudo) > ", str(name))
            if (defi) == self.level :
                score = 0
            else :
                score = self.level - 1
            Database(name,score)
            screen = pygame.display.set_mode((500,600))
           
playerOne = Sequence()

#=============================================================================================================  Variables
menu , pause , play , aide, score, playmenu, challenge, speedmenu, sensgame =  1 , 0 , 0, 0, 0, 0, 0, 0, 0  # Acces aux boucles 
choix_menu, choix_playmenu, choix_challenge, choix_speed, choix_blind = 0, 0, 0, 0, 0 #choix des menus
tourOrdi , tourPlayer = 0,0 #tour pour les séquences
nosound, blindness = 0,0 #Event Game
#------    Sélection Menu
x = -0
w = 1

x2 = -0
w2 = 1

x3 = -0
w3 = 1

x4 = -0
w4 = 1

x5 = -0
w5 = 1

#------ Mise à jours des variables de jeux
a = 0
seq_ordi, seq_joueur = '' , ''
compteur , go = 0, 0
dataload = 1
#=========================================================================================== Création de la fenètre principal

screen = pygame.display.set_mode((500,600))

#========================================================================================================== Boucle principale    

while True :
    
    while menu :
        speed = 75
        
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == KEYDOWN :
                if event.key == K_UP:
                        choix_menu -= 1
                if event.key == K_DOWN:
                        choix_menu += 1
               
            if choix_menu == 4 :
                choix_menu = 0
            if choix_menu == -1:
                choix_menu = 3        
        
        if x == 5 :
            w = -1
        if x == 0 :
            w = 1
        x += w
        screen.fill(noir)
        cadre = Draw_rect().gen((46,52,54),((0,200),(500,275)))
        screen.blit((Image(titre1)),(10,0)) 
        textMenu = Texte('Menu principal', 75, noir, (cadre.centerx,cadre.top + 45)).affiche()
        textMenu = Texte('Menu principal', 70, blanc, (cadre.centerx,cadre.top + 40)).affiche()        
        textMenu = Texte('Jouer', 60, noir, (cadre.centerx,cadre.top + 100)).affiche()
        textMenu = Texte('Aide', 60, noir, (cadre.centerx,cadre.top + 150)).affiche()
        textMenu = Texte('Score', 60, noir, (cadre.centerx,cadre.top + 200)).affiche()
        textMenu = Texte('Quitter', 60, noir, (cadre.centerx,cadre.top + 250)).affiche()
            
        if choix_menu == 0 :           
            textMenu = Texte('Jouer', 60+x, jaune, (cadre.centerx,cadre.top + 100)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                menu = 0
                playmenu = 1
                #play = 1
                #tourOrdi = 1
                                
        if choix_menu == 1 :
            textMenu = Texte('Aide', 60+x, vert, (cadre.centerx,cadre.top + 150)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                menu = 0        
                aide = 1 
                print("[Logs] > Menu aide ouvert.")
        if choix_menu == 2:
            textMenu = Texte('Score', 60+x, bleu, (cadre.centerx,cadre.top + 200)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                menu = 0
                score = 1
                dataload = 1
        if choix_menu == 3 :
            textMenu = Texte('Quitter', 60+x, rouge, (cadre.centerx,cadre.top + 250)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                exit()
        
        pygame.time.wait(speed)
        pygame.display.flip()
                

    while playmenu:
        
        speed = 75
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                playmenu = 0
                choix_menu = 0
                menu = 1
                choix_playmenu = 0
                print("[Logs] > Menu principale ouvert.")
            if event.type == KEYDOWN :
                if event.key == K_UP:
                        choix_playmenu -= 1
                if event.key == K_DOWN:
                        choix_playmenu += 1
            
            if choix_playmenu == 4 :
                choix_playmenu = 0
            if choix_playmenu == -1:
                choix_playmenu = 3    
        
        if x2 == 3 :
            w2 = -1
        if x2 == 0 :
            w2 = 1
        x2 += w2
        screen.fill(noir)
        cadre = Draw_rect().gen((46,52,54),((0,200),(500,275)))
        screen.blit((Image(titre1)),(10,0)) 
        textMenu = Texte('Options de jeu', 75, noir, (cadre.centerx,cadre.top + 45)).affiche()
        textMenu = Texte('Options de jeu', 70, blanc, (cadre.centerx,cadre.top + 40)).affiche()        
        textMenu = Texte('Classique', 60, noir, (cadre.centerx,cadre.top + 100)).affiche()
        textMenu = Texte('Challenges', 60, noir, (cadre.centerx,cadre.top + 150)).affiche()
        textMenu = Texte('Speed Run', 60, noir, (cadre.centerx,cadre.top + 200)).affiche()
        textMenu = Texte('No Sense', 60, noir, (cadre.centerx,cadre.top + 250)).affiche()
            
        if choix_playmenu == 0 :           
            textMenu = Texte('Classique', 60+x2, vert, (cadre.centerx,cadre.top + 100)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                playmenu = 0
                play = 1
                tourOrdi = 1
                print("[Logs] > Jeu en cours d'execution..")
                                
        if choix_playmenu == 1 :
            textMenu = Texte('Challenges', 60+x2, jaune, (cadre.centerx,cadre.top + 150)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                challenge = 1
                playmenu = 0
                print("[Logs] > Menu challenge ouvert.")

        if choix_playmenu == 2 :
            textMenu = Texte('Speed Run', 60+x2, orange, (cadre.centerx,cadre.top + 200)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                playmenu = 0
                speedmenu = 1
                print("[Logs] > Menu SpeedRun ouvert.")
        
        if choix_playmenu == 3:
            textMenu = Texte('No Sense', 60+x2, rouge, (cadre.centerx,cadre.top + 250)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                playmenu = 0
                sensgame = 1
                print("[Logs] > Menu des sens ouvert.")
        
        pygame.time.wait(speed)
        pygame.display.flip()

####################################################################################################

    while challenge:
        
        speed = 75
        
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                challenge = 0
                playmenu = 1
                choix_challenge = 0
                print("[Logs] > PlayMenu ouvert.")
            if event.type == KEYDOWN :
                if event.key == K_UP:
                        choix_challenge -= 1
                if event.key == K_DOWN:
                        choix_challenge += 1
               
            if choix_challenge == 3 :
                choix_challenge = 0
            if choix_challenge == -1:
                choix_challenge = 2      
        
        if x3 == 5 :
            w3 = -1
        if x3 == 0 :
            w3 = 1
        x3 += w3
        screen.fill(noir)
        cadre = Draw_rect().gen((46,52,54),((0,200),(500,275)))
        screen.blit((Image(titre1)),(10,0))
        textMenu = Texte('Liste des Challenges', 70, noir, (cadre.centerx,cadre.top + 45)).affiche()
        textMenu = Texte('Liste des Challenges', 67, blanc, (cadre.centerx,cadre.top + 40)).affiche()
        textMenu = Texte('Challenge 10', 60, noir, (cadre.centerx,cadre.top + 125)).affiche()
        textMenu = Texte('Challenge 50', 60, noir, (cadre.centerx,cadre.top + 175)).affiche()
        textMenu = Texte('Challenge 100', 60, noir, (cadre.centerx,cadre.top + 225)).affiche()
        if choix_challenge == 0 :
            textMenu = Texte('Challenge 10', 60+x3, jaune, (cadre.centerx,cadre.top + 125)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                challenge = 0
                play = 1
                tourOrdi = 1
                defi = 10
                playerOne.level = defi
                
                
        if choix_challenge == 1:
            textMenu = Texte('Challenge 50', 60+x3, orange, (cadre.centerx,cadre.top + 175)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                challenge = 0
                play = 1
                tourOrdi = 1
                defi = 50
                playerOne.level = defi

        if choix_challenge == 2:
            textMenu = Texte('Challenge 100', 60+x3, rouge, (cadre.centerx,cadre.top + 225)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                challenge = 0
                play = 1
                tourOrdi = 1
                defi = 100
                playerOne.level = defi
        
        pygame.time.wait(speed)
        pygame.display.flip()

    while speedmenu:
        
        speed = 75
        
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                speedmenu = 0
                playmenu = 1
                choix_speed = 0
                print("[Logs] > PlayMenu ouvert.")
            if event.type == KEYDOWN :
                if event.key == K_UP:
                        choix_speed -= 1
                if event.key == K_DOWN:
                        choix_speed += 1
               
            if choix_speed == 3 :
                choix_speed = 0
            if choix_speed == -1:
                choix_speed = 2      
        
        if x4 == 5 :
            w4 = -1
        if x4 == 0 :
            w4 = 1
        x4 += w4
        screen.fill(noir)
        cadre = Draw_rect().gen((46,52,54),((0,200),(500,275)))
        screen.blit((Image(titre1)),(10,0))
        textMenu = Texte('Liste des SpeedRun', 70, noir, (cadre.centerx,cadre.top + 45)).affiche()
        textMenu = Texte('Liste des SpeedRun', 67, blanc, (cadre.centerx,cadre.top + 40)).affiche()
        textMenu = Texte('SpeedRun [x2]', 60, noir, (cadre.centerx,cadre.top + 125)).affiche()
        textMenu = Texte('SpeedRun [x3]', 60, noir, (cadre.centerx,cadre.top + 175)).affiche()
        textMenu = Texte('SpeedRun [x5]', 60, noir, (cadre.centerx,cadre.top + 225)).affiche()
        if choix_speed == 0 :
            textMenu = Texte('SpeedRun [x2]', 60+x4, jaune, (cadre.centerx,cadre.top + 125)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                rundefi = 1
                play = 1
                tourOrdi = 1
                speedmenu = 0
                
                
        if choix_speed == 1:
            textMenu = Texte('SpeedRun [x3]', 60+x4, orange, (cadre.centerx,cadre.top + 175)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                rundefi = 2
                play = 1
                tourOrdi = 1
                speedmenu = 0

        if choix_speed == 2:
            textMenu = Texte('SpeedRun [x5]', 60+x4, rouge, (cadre.centerx,cadre.top + 225)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                rundefi = 3
                play = 1
                tourOrdi = 1
                speedmenu = 0
        
        pygame.time.wait(speed)
        pygame.display.flip()

    while sensgame:
        
        speed = 75
        
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                sensgame = 0
                playmenu = 1
                choix_blind = 0
                print("[Logs] > PlayMenu ouvert.")
            if event.type == KEYDOWN :
                if event.key == K_UP:
                        choix_blind -= 1
                if event.key == K_DOWN:
                        choix_blind += 1
               
            if choix_blind == 3 :
                choix_blind = 0
            if choix_blind == -1:
                choix_blind = 2      
        
        if x5 == 5 :
            w5 = -1
        if x5 == 0 :
            w5 = 1
        x5 += w5
        screen.fill(noir)
        cadre = Draw_rect().gen((46,52,54),((0,200),(500,275)))
        screen.blit((Image(titre1)),(10,0))
        textMenu = Texte('Liste des SenseGame', 70, noir, (cadre.centerx,cadre.top + 45)).affiche()
        textMenu = Texte('Liste des SenseGame', 67, blanc, (cadre.centerx,cadre.top + 40)).affiche()
        textMenu = Texte('Blindness', 60, noir, (cadre.centerx,cadre.top + 125)).affiche()
        textMenu = Texte('Soundless', 60, noir, (cadre.centerx,cadre.top + 175)).affiche()
        textMenu = Texte('Soon...', 60, noir, (cadre.centerx,cadre.top + 225)).affiche()
        if choix_blind == 0 :
            textMenu = Texte('Blindness', 60+x5, jaune, (cadre.centerx,cadre.top + 125)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                blindness = 1
                play = 1
                tourOrdi = 1
                sensgame = 0
                
                
        if choix_blind == 1:
            textMenu = Texte('Soundless', 60+x5, orange, (cadre.centerx,cadre.top + 175)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                nosound = 1
                play = 1
                tourOrdi = 1
                sensgame = 0

        if choix_blind == 2:
            textMenu = Texte('Soon...', 60+x5, rouge, (cadre.centerx,cadre.top + 225)).affiche()
            if event.type == KEYDOWN and event.key == K_RETURN :
                print("[Logs] > Jeu indisponible.")
        
        pygame.time.wait(speed)
        pygame.display.flip()

#################################################################################################################

    while aide:
        screen.fill(noir)
        cadre = Draw_rect().gen((46,52,54),((0,200),(500,250)))
        textMenu = Texte('Commandes :', 40, noir, (125,cadre.top + 30)).affiche()
        screen.blit((Image(help)),(0,200))
        screen.blit((Image(titre1)),(10,0))
        
        pygame.time.wait(speed)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE :
                aide = 0
                menu = 1
        


    while score:
        
        screen.fill(noir)
        cadre = Draw_rect().gen((46,52,54),((0,100),(500,400)))
        textMenu = Texte('Meilleurs Scores', 40, blanc, (cadre.centerx,cadre.top + 30)).affiche()
        textMenu = Texte('____________________________________', 40, noir, (cadre.centerx,cadre.top + 35)).affiche()
        pygame.time.wait(speed)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE :
                score = 0
                menu = 1
                dataload = 0
        
        if dataload == 1:
            dataload = 0
            loading = ()
            ScorePlayer = []
            with open('Game/database.yaml') as f:
            
                topscores = yaml.load_all(f, Loader=yaml.SafeLoader)

                for doc in topscores:
                
                    for k, v in doc.items():
                        print("[Logs] > ", k, "->", v)
                        
                        v = str(v).replace("{'score': '", "")
                        v = v.replace("'}", "")
                        
                        loading += (k,)
                        loading += (int(v),)

                        ScorePlayer.append(loading)

                        loading = ()
                        print("[Logs] (loading) > " + str(loading))
                        print("[Logs] (ScorePlayer) > " + str(ScorePlayer))
                        ScorePlayer.sort(key=lambda x:x[1])
                        ScorePlayer.reverse()
                        print("[Logs] (ScorePlayer) > " + str(ScorePlayer))

            #--------------------------------------------------

            if len(ScorePlayer) >= 1:
                print("[Logs] > " + str(ScorePlayer[0]))
                ScorePlayerAffichage1 = str(ScorePlayer[0][1])
                print("[Logs] > " + ScorePlayerAffichage1)
            if len(ScorePlayer) >= 2:
                print("[Logs] > " + str(ScorePlayer[1]))
                ScorePlayerAffichage2 = str(ScorePlayer[1][1])
                print("[Logs] > " + ScorePlayerAffichage2)
            if len(ScorePlayer) >= 3:
                print("[Logs] > " + str(ScorePlayer[2]))
                ScorePlayerAffichage3 = str(ScorePlayer[2][1])
                print("[Logs] > " + ScorePlayerAffichage3)
            if len(ScorePlayer) >= 4:
                print("[Logs] > " + str(ScorePlayer[3]))
                ScorePlayerAffichage4 = str(ScorePlayer[3][1])
                print("[Logs] > " + ScorePlayerAffichage4)
            if len(ScorePlayer) >= 5:
                print("[Logs] > " + str(ScorePlayer[4]))
                ScorePlayerAffichage5 = str(ScorePlayer[4][1])
                print("[Logs] > " + ScorePlayerAffichage5)
            if len(ScorePlayer) >= 6:
                print("[Logs] > " + str(ScorePlayer[5]))
                ScorePlayerAffichage6 = str(ScorePlayer[5][1])
                print("[Logs] > " + ScorePlayerAffichage6)
            if len(ScorePlayer) >= 7:
                print("[Logs] > " + str(ScorePlayer[6]))
                ScorePlayerAffichage7 = str(ScorePlayer[6][1])
                print("[Logs] > " + ScorePlayerAffichage7)
            if len(ScorePlayer) >= 8:
                print("[Logs] > " + str(ScorePlayer[7]))
                ScorePlayerAffichage8 = str(ScorePlayer[7][1])
                print("[Logs] > " + ScorePlayerAffichage8)
            if len(ScorePlayer) >= 9:
                print("[Logs] > " + str(ScorePlayer[8]))
                ScorePlayerAffichage9 = str(ScorePlayer[8][1])
                print("[Logs] > " + ScorePlayerAffichage9)
            if len(ScorePlayer) >= 10:
                print("[Logs] > " + str(ScorePlayer[9]))
                ScorePlayerAffichage10 = str(ScorePlayer[9][1])
                print("[Logs] > " + ScorePlayerAffichage10)
            dataloaded = 1    

        if dataloaded == 1:
            #dataloaded = 0
            textMenu = Texte("Top 1 :", 40, jaune, (75,cadre.top + 75)).affiche()
            textMenu = Texte("Top 2 :", 40, argent, (75,cadre.top + 105)).affiche()
            textMenu = Texte("Top 3 :", 40, bronze, (75,cadre.top + 135)).affiche()
            textMenu = Texte("Top 4 :", 40, blanc, (75,cadre.top + 165)).affiche()
            textMenu = Texte("Top 5 :", 40, blanc, (75,cadre.top + 195)).affiche()
            textMenu = Texte("Top 6 :", 40, blanc, (75,cadre.top + 225)).affiche()
            textMenu = Texte("Top 7 :", 40, blanc, (75,cadre.top + 255)).affiche()
            textMenu = Texte("Top 8 :", 40, blanc, (75,cadre.top + 285)).affiche()
            textMenu = Texte("Top 9 :", 40, blanc, (75,cadre.top + 315)).affiche()
            textMenu = Texte("Top 10:", 40, blanc, (75,cadre.top + 345)).affiche()

            if len(ScorePlayer) >= 1:
                textMenu = Texte(str(ScorePlayer[0][0]) + " | " + str(ScorePlayerAffichage1), 40, jaune, (cadre.centerx,cadre.top + 75)).affiche()
            if len(ScorePlayer) >= 2:        
                textMenu = Texte(str(ScorePlayer[1][0]) + " | " + str(ScorePlayerAffichage2), 40, argent, (cadre.centerx,cadre.top + 105)).affiche()
            if len(ScorePlayer) >= 3:               
                textMenu = Texte(str(ScorePlayer[2][0]) + " | " + str(ScorePlayerAffichage3), 40, bronze, (cadre.centerx,cadre.top + 135)).affiche()
            if len(ScorePlayer) >= 4:                
                textMenu = Texte(str(ScorePlayer[3][0]) + " | " + str(ScorePlayerAffichage4), 40, blanc, (cadre.centerx,cadre.top + 165)).affiche()
            if len(ScorePlayer) >= 5:                
                textMenu = Texte(str(ScorePlayer[4][0]) + " | " + str(ScorePlayerAffichage5), 40, blanc, (cadre.centerx,cadre.top + 195)).affiche()
            if len(ScorePlayer) >= 6:                
                textMenu = Texte(str(ScorePlayer[5][0]) + " | " + str(ScorePlayerAffichage6), 40, blanc, (cadre.centerx,cadre.top + 225)).affiche()
            if len(ScorePlayer) >= 7:                
                textMenu = Texte(str(ScorePlayer[6][0]) + " | " + str(ScorePlayerAffichage7), 40, blanc, (cadre.centerx,cadre.top + 255)).affiche()
            if len(ScorePlayer) >= 8:                
                textMenu = Texte(str(ScorePlayer[7][0]) + " | " + str(ScorePlayerAffichage8), 40, blanc, (cadre.centerx,cadre.top + 285)).affiche()
            if len(ScorePlayer) >= 9:                
                textMenu = Texte(str(ScorePlayer[8][0]) + " | " + str(ScorePlayerAffichage9), 40, blanc, (cadre.centerx,cadre.top + 315)).affiche()
            if len(ScorePlayer) >= 10:                
                textMenu = Texte(str(ScorePlayer[9][0]) + " | " + str(ScorePlayerAffichage10), 40, blanc, (cadre.centerx,cadre.top + 345)).affiche()
            pygame.display.flip()
                        
    



    while play:
        
        if playerOne.level == 0:
            play , tourOrdi ,menu = 0 , 0 , 1
            playerOne = Sequence()
        
        
        compteur = 0
        seq_ordi = ''
        seq_joueur = ''
        
        while tourOrdi :
            
            if rundefi == 0:
                speed = 250
            if rundefi == 1:
                speed = 125
            if rundefi == 2:
                speed = 85
            if rundefi == 3:
                speed = 50
            
            screen.fill(noir)
            Draw_rect().gen_bg()
                       
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    play = 0
                    tourOrdi = 0
                    menu = 1
                    
                if event.type == KEYDOWN and event.key == K_SPACE :
                    if seq_ordi == '' :
                        seq_ordi = playerOne.gen_seq()
                        go = 1

            if go == 1:
                if a % 2 == 0 :
                
                    if compteur != playerOne.level :
                        if nosound != 1:
                            liste_son[int(seq_ordi[compteur])].play()
                        if blindness != 1:
                            Draw_rect().gen(couleur_clair[int(seq_ordi[compteur])],liste_pos[int(seq_ordi[compteur])])
                        compteur += 1
                            
                
                
                a += 1
                if compteur  == playerOne.level :
                    tourOrdi = 0
                    tourPlayer = 1
                    go = 0 
                    print("[Logs] > Tour du joueur en cours..")

            screen.blit((Image(centre)),(0,0))
            screen.blit((Image(fond)),(0,0))
            screen.blit((Image(titre)),(0,500))
            extMenu = Texte('{}'.format(playerOne.level), 50, blanc, (425,565)).affiche()
            
            pygame.display.flip()
            pygame.time.wait(speed)
        while tourPlayer :
            speed = 80
            screen.fill(noir)
            Draw_rect().gen_bg()
            
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    tourPlayer = 0
                    play = 0
                    menu = 1

                if event.type == KEYDOWN :
                    if event.key == K_UP:
                        seq_joueur += '1'
                        son1.play()
                        #Draw_rect().gen(couleur_clair[0],liste_pos[0])
                        Draw_rect().gen(couleur_clair[1],liste_pos[1])
                        print("[Logs] (Séquence) > " + seq_joueur)
                    if event.key == K_DOWN:    
                        seq_joueur += '2'
                        son2.play()
                        #Draw_rect().gen(couleur_clair[1],liste_pos[1])
                        Draw_rect().gen(couleur_clair[2],liste_pos[2])
                        print("[Logs] (Séquence) > " + seq_joueur)
                    if event.key == K_LEFT:
                        seq_joueur += '0'
                        son3.play()
                        #Draw_rect().gen(couleur_clair[2],liste_pos[2])
                        Draw_rect().gen(couleur_clair[0],liste_pos[0])
                        print("[Logs] (Séquence) > " + seq_joueur)
                    if event.key == K_RIGHT:
                        seq_joueur += '3'
                        son4.play()
                        #Draw_rect().gen(couleur_clair[3],liste_pos[3])
                        Draw_rect().gen(couleur_clair[3],liste_pos[3])
                        print("[Logs] (Séquence) > " + seq_joueur)
                       
                           
            if len(seq_joueur) == len(seq_ordi):        #si la longueur de la séquence du joueur est égal a celle de l'ordi, on compare
                
                print("[Logs] > " + seq_joueur + " | " + seq_ordi)
                if seq_joueur != seq_ordi :
                    playerOne.change_level(0)
                    play , tourOrdi ,menu = 0 , 0 , 1
                    print("[Logs] > Séquence échoué")
                    playerOne = Sequence()
                if seq_joueur == seq_ordi :
                    playerOne.change_level(1)
                    print("[Logs] > Séquence réussi")
                    print("[Logs] > +1 level")
                
                
                
                tourPlayer = 0
                tourOrdi = 1
       
            screen.blit((Image(centre)),(0,0))
            screen.blit((Image(fond)),(0,0))
            screen.blit((Image(titre)),(0,500))
            extMenu = Texte('{}'.format(playerOne.level), 50, blanc, (425,565)).affiche()
            pygame.time.wait(speed)
            pygame.display.flip()
