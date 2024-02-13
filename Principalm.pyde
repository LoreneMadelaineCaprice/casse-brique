from __future__ import unicode_literals  #pour utiliser unicode et donc les accents et caracteres speciaux 
from Paddle import Paddle #import de la classe Paddle
from Ball import Ball #import de la classe Ball
from Brick import Brick #import de la classe Brick

playingGame = False
Win = False
bricks = []  #création de la lste
score = 0 #initialisation du score à 0
vies = 3 #initialisation à 3 vies
niv = 1 #on initialise le niveau à 1

def setup():
    global paddle, ball # on déclare la variable paddle comme globale
    size(605,400)
    paddle = Paddle() # on crée l'objet paddle
    ball = Ball()
    # appel de la fonction addBrick pour ajouter les briques
    for x in range (5, width - 80, 75):
        #addBrick(x + 37.5, 50, 3)
        #addBrick(x + 37.5, 70, 2)
        addBrick(x + 37.5, 90, 1) 
    #ball.vel *= 0.4 

def draw():
    background(0,0,0)
    Win = False
    #Perdu = False
    global score, vies, playingGame, niv
    #niv = 1 #on initialise le niveau à 1 problème du coup
    
    ##un compteur au départ
    #if mousePressed:
    #    global playingGame
    #   for i in range (4):
    #        textSize(76)
    #       fill(250)
    #        textAlign(CENTER)
    #        text(i,302.5,200)
    #    playingGame = True   
    
    textSize(20)
    fill(250)
    textAlign(LEFT)
    #if score < 0: #le score ne peut pas être négatif
    #    score = 0
    text("Score : "+str(score),12,30) #affichage du score

    textAlign(RIGHT)
    text("Vies : "+str(vies),597,30) #affichage des vies restantes

    textAlign(CENTER)
    text("Niveau "+str(niv),302.5,30) #affichage du niveau actuel
    
    #appel des méthodes pour le paddle
    paddle.display()
    if playingGame:
        paddle.checkEdges()
        paddle.update()
    #appel des méthodes pour la balle
    ball.display()
    if playingGame:
        ball.checkEdges()
        ball.update()
    if (ball.meets(paddle)): #contact entre la balle et le socle
        if (ball.dir.y > 0):
            ball.dir.y *= -1

    for i in range (len(bricks)):
        bricks[i].display()
    for i in range (len(bricks)-1,-1,-1):  #parcourt liste des briques à l'envers
        if (ball.meets(bricks[i])):  #si collision détectée
        
            if bricks[i].hits == 3:  #la brique touchée est violette donc il faut 3 coups pour la détruire
                bricks[i].col = Brick.COLORS[2] # la couleur change pour rose
                bricks[i].hits = 2
                #score = score + 5
                ball.dir.y*=-1
                
            elif bricks[i].hits == 2:  #la brique touchée est rose donc il faut 2 coups pour la détruire
                bricks[i].col = Brick.COLORS[1] # la couleur change pour vert
                bricks[i].hits = 1
                #score = score + 5
                ball.dir.y*=-1

            else:  #la brique touchée est vert donc il faut 1 coup pour la détruire
                score = score + 10
                bricks.pop(i)  #sup brique touchée
                #del bricks[i]
                ball.dir.y*=-1
            
                
##sans changement de couleur etc                        
    # for i in range (len(bricks)-1,-1,-1):  #parcourt liste des briques à l'envers
    #     if (ball.meets(bricks[i])):  #si collision détectée
    #         score = score + 10
    #         bricks.pop(i)  #sup brique touchée
    #         #del bricks[i]
    #         ball.dir.y*=-1
                
            
    #if ball.pos.y > 400 and len(bricks) != 0: #si la balle ne se trouve plus dans la fenetre, le joueur perd
    #    textSize(76)
    #    fill(250)
    #    textAlign(CENTER)
   #     text("Perdu!",302.5,200)
   
    if ball.pos.y > 400 and len(bricks) != 0: #si la balle ne se trouve plus dans la fenetre, le joueur perd
        vies = vies - 1
        #score = score - 20
        textSize(20)
        fill(250)
        textAlign(RIGHT)
        text(str(vies),600,30)
        ball.pos.x = 302.5 #retour de la ball au centre de l'écran
        ball.pos.y = 200    
        playingGame = False
        
        #if vies <= 0:
        #    textSize(76)
        #    fill(250)
        #    textAlign(CENTER)
        #    text("Perdu!",302.5,200)
        #    good()
        #    playingGame = False
        #    #Perdu = True
        #    #playingGame = True
            
    
    if vies <= 0:
        bad()
        textSize(76)
        fill(250)
        textAlign(CENTER)
        text("Perdu !",302.5,200)
    
        textSize(25)
        text("Vous avez obtenu un score de : "+str(score),300,250) #affichage du score à la fin de la partie
        
        playingGame = False
        #Perdu = True
        #playingGame = True
        
    #if vies == 0:
    #    textSize(76)
    #    fill(250)
    #    textAlign(CENTER)
    #    text("Perdu!",302.5,200)
            
    #if len(bricks) == 0:
    #    textSize(76)
    #    fill(250)
    #    textAlign(CENTER)
    #    text("Gagné !",302.5,200)
    #    textSize(20)
    #    text("Cliquer sur la touche 'a' pour changer de niveau",302.5,250) #permet de changer de fond
        
    #    Win = True
    #    #if key == "a" or key == "A": #la touche A permet de changer le niveau
        
    #    if Win: #la touche A permet de changer le niveau
    #        niv = niv + 1
    #        good()
    #        textSize(46)
    #        fill(250)
    #        textAlign(CENTER)
    #        text("Niveau superieur !",302.5,180)
    #        text("niveau "+str(niv),302.5,220)
    #        textSize(20)
    #        text("Cliquer sur la touche 'a' pour afficher le niveau",302.5,250) #permet de changer de fond
            #restart()
            
            
            #if key == "a" or key == "A": #la touche A permet d'afficher le nouveau niveau
            
            #changer vitesse balle + afficher tout comme avant avec le meme score

###mode admin ne fonctionnne pas            
    # if key == "x" or key == "X": #la touche x permet de changer de niveau manuellement
    #     if keyCode==UP:
            
    #         playingGame = False
    #         setup() #réinitialise le jeu 
    #         niv = niv + 1 #augmentation du niveau
    #         niveau()
        
    #     elif keyCode==DOWN:
    #         playingGame = False
    #         setup() #réinitialise le jeu
    #         niv = niv - 1 #diminuation du niveau   
    #         niveau()             
     

#augmenter manuellement les niveaux
    #if key == "x" or key == "X": #la touche x permet de changer de niveau manuellement
    if keyCode==UP:
        niv = niv + 1 #augmentation du niveau à l'infinie ???
        playingGame = False
        setup() #réinitialise le jeu 
        niveau()
        
    elif keyCode==DOWN:
        playingGame = False
        setup() #réinitialise le jeu
        niv = niv - 1 #diminuation du niveau   
        niveau()   
        
        
    
    if len(bricks) == 0:
        good()
        textSize(76)
        fill(250)
        textAlign(CENTER)
        text("Gagné !",302.5,180)
        #text(u"Gagné !",302.5,180)  # autre syntaxe si  la premiere ligne n'est pas ajoutee 
        #niv = niv + 1
        textSize(46)
        fill(250)
        textAlign(CENTER)
        text("Niveau superieur !",302.5,230)
        textSize(20)
        text("Cliquer sur la touche 'a' pour afficher le niveau",302.5,280) #permet de changer de fond
        #restart()

###changement niveau sans la focntion            
        # if key == "a" or key == "A": #la touche A permet d'afficher le nouveau niveau
        #     playingGame = False
        #     setup() #réinitialise le jeu avec le score en tête
        #     niv = niv + 1 #augmentation du niveau
            
        #     if niv == 2:
        #         for x in range (5, width - 80, 75):
        #             addBrick(x + 37.5, 70, 2)
            
        #     if niv == 3:
        #         for x in range (5, width - 80, 75):
        #             addBrick(x + 37.5, 70, 2)
        #             addBrick(x + 37.5, 50, 3)
                    
        #     if niv >= 4:
        #         for x in range (5, width - 80, 75):
        #             addBrick(x + 37.5, 70, 2)
        #             addBrick(x + 37.5, 50, 3)  
        #         ball.vel *= 0.4*niv #la vitesse de la balle dépend du niveau atteind
                
        #     if niv >= 10 :
        #         self.w = 20 #la taille de la raquette diminue
        
        if key == "a" or key == "A": #la touche A permet d'afficher le nouveau niveau
            playingGame = False
            setup() #réinitialise le jeu avec le score en tête
            niv = niv + 1 #augmentation du niveau
            niveau()
            
        #chag avec touche espace     
        # if keyCode==ESPACE: #la touche espace permet d'afficher le nouveau niveau
        #     playingGame = False
        #     setup() #réinitialise le jeu avec le score en tête
        #     niv = niv + 1 #augmentation du niveau
        #     ball.vel *= niv #la vitesse de la balle dépend du niveau atteind

    #if Win == True:
    #    niv = niv + 1
    #    #vert()
    #    #addBrick(x + 37.5, 110, 3)
    #    textSize(76)
    #    fill(250)
    #    textAlign(CENTER)
    #    text("NOUVEAU NIV !",302.5,200)
        
        
    # if key == "p" and key == "P": #la touche P permet de changer de niveau
    #     playingGame = False
        
    #     textSize(76)
    #     fill(250)
    #     textAlign(CENTER)
    #     text("non !",302.5,200)
    #     setup() #réinitialise le jeu avec le score en tête
    #     niv = niv + 1

     
def niveau():
    if niv == 2:
        for x in range (5, width - 80, 75):
            addBrick(x + 37.5, 70, 2)
    
    if niv == 3:
        for x in range (5, width - 80, 75):
            addBrick(x + 37.5, 70, 2)
            addBrick(x + 37.5, 50, 3)
            
    if niv >= 4:
        for x in range (5, width - 80, 75):
            addBrick(x + 37.5, 70, 2)
            addBrick(x + 37.5, 50, 3)  
        ball.vel *= 0.4*niv #la vitesse de la balle dépend du niveau atteind
        
    if niv >= 10 :
        paddle.w = 60 #la taille de la raquette diminue
              
# fonction créant et stockant les briques dans la liste
def addBrick(x, y, hits): #hits permet de definir la couleur de la brique
    brick = Brick(x, y, hits)
    bricks.append(brick)

# détection des mouvements touches a et d
#def keyPressed():
#    if key == "a" or key == "A":
#        paddle.isMovingLeft = True #la touche "a" fait bouger le socle à gauche
#    elif key == "d" or key == "D":
#        paddle.isMovingRight = True #la touche "d" fait bouger le socle à droite
        
# détection des mouvements touches <- et ->
def keyPressed():
    if keyCode==LEFT:
        paddle.isMovingLeft = True #la touche fleche gauche du clavier fait bouger le socle à gauche
    elif keyCode==RIGHT: 
        paddle.isMovingRight = True #la touche fleche droite du clavier fait bouger le socle à droite
#pause ?
        
#annulation des mouvements quand on relâche la touche
def keyReleased(): #tant qu'on maintient enfoncé la touche, le socle continu d'avancer
    paddle.isMovingRight = False
    paddle.isMovingLeft = False

def mousePressed(): #le jeu commence au clic de la souris
    global playingGame
    delay(300) #temps de flottement avanat le début du jeu
    playingGame = True

    
    
    
    
    
    
    
    
    
###############################################################################################################################################################################
def good():
    #background(0,0,0)
    background(152,190,100)
    
def bad():
    #background(0,0,0)
    background(255,100,80)
    
    
#affiche un message lorsque la liste bricks est vide, donc que le joueur a detruit toutes les briques        
#def Won(bricks):
#    if len(bricks)==0:
#        text("Gagné",100,100)
        

#fonction arretant le jeu
#def looseGame(ball):
#    if ball.pos.y > 400 : #si la balle ne se trouve plus dans la fenetre
#        textSize(76)
#        fill(250)
#        textAlign(CENTER)
#        text("Perdu !",302.5,200)
#        playingGame = False



#fonction arretant le jeu
#def looseGame(ball,paddle):
#    if ball.pos.y > paddle.pos.y + paddle.h :
#        text("Perdu",100,70)
#        return True
    
#def vies():
#    vies=3
#    if looseGame(ball,paddle)==True:
#        vies=vies-1
#        if vies==0:
#            text("Perdu",100,70)
#            playingGame=False
