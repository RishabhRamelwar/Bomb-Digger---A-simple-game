import pygame, sys                              # Importing pygame and other modules 
import random
from pygame.locals import *


pygame.init()
FPS = 100
Clock = pygame.time.Clock()


screen= pygame.display.set_mode((500, 400))     # Main screen length and width
pygame.display.set_caption('Bomb Digger')


Black=(  0,   0,   0)
Blue=(  0,  0, 255) 
Green=(  0, 128,   0)                           # Variables storing different colours
Red=(255,   0,   0)                             
White=(255, 255, 255)
Yellow=(255, 255,   0)


BASICFONT = pygame.font.Font('freesansbold.ttf', 16)          # Fonts used in the game
bigfont= pygame.font.Font('freesansbold.ttf', 25)


score = 0                                       # Initial score
nextlevel = 500
level=1                                         # Initial level


hero = pygame.image.load('hero.png')
bomb = pygame.image.load('bomb.png')            # Images loaded to game
heart= pygame.image.load('heart.png')


heartx=random.randint(0,470)
hearty=-150
bomby=-50
bombx=random.randint(0,470)
herox = 0
heroy = 300                                   # Initial Position of the characters in the game
herox_change=0
heroy_change=0
bombx_change=0
bomby_change=0
heartx_change=0
hearty_change=0


l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

flag=True
while (flag==True):
    
    screen.fill(White)
    scoreSurf = BASICFONT.render('Score: ' + str(score), 1, Black)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (400, 10)                                            # Main Screen Display
    screen.blit(scoreSurf, scoreRect)
    welcomeSurf=bigfont.render('WELCOME TO THE GAME',1,Blue)
    welcomeRect= welcomeSurf.get_rect()
    welcomeRect.topleft = (0, 10)
    screen.blit(welcomeSurf, welcomeRect)
    levelSurf = bigfont.render('Level :- '+ str(level),1,Blue)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (370,30)
    screen.blit(levelSurf, levelRect)

    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:                    # For Moving The Main Character   
                herox_change=-25
            if event.key == K_RIGHT:
                herox_change=25
        herox+=herox_change


    if bomby<=400:
        bomby_change=5                     # Downward Movement of Bomb
    else:
        bomby=400
    bomby+=bomby_change
    if herox==550:
        herox=-25
    elif herox==-50:
        herox=525
    if hearty<=500:
        hearty_change=3                    # Downward Movement of Heart
    elif hearty>500:
        heartx=random.randint(0,470)            
        hearty=-150
    hearty+=hearty_change

    
    screen.blit(heart, (heartx, hearty))
    screen.blit(bomb, (bombx, bomby))                           # Making changes in position of characters 
    pygame.draw.rect(screen, Black, (0, 360, 500, 50))
    screen.blit(hero, (herox, heroy))

    
    if bomby==405:
        bomby=-50
        bombx=random.randint(0,470)
    screen.blit(heart, (heartx, hearty))
    screen.blit(bomb, (bombx, bomby))
    pygame.draw.rect(screen, Black, (0, 360, 500, 50))
    screen.blit(hero, (herox, heroy))

    
    if bomby==400:
            score+=10                                    # Increment in score by 10 when a bomb is dodged
    for a in l1:
        if heartx==herox and hearty==(heroy-45):
            score+=50
            hearty=450
        elif heartx==herox-a and hearty==(heroy-45):     # Increment in score by 50 when a heart is collected
            score+=50
            hearty=450
        elif heartx==herox+a and hearty==(heroy-45):
            score+=50
            hearty=450


    if score >= nextlevel:                              # Increment in level at every 500 score
        level +=1
        nextlevel+=500
        FPS +=30                                      # Speed of bombs increases
        
            
    for i in l1:
        if bombx==herox and bomby==(heroy-45):
            exitSurf=bigfont.render('! GAME OVER ! your score = ' + str(int(score)),1,Red)
            exitRect= exitSurf.get_rect()
            exitRect.center=(250,200)
            screen.blit(exitSurf, exitRect)
            flag=False
        elif bombx==herox-i and bomby==(heroy-45):
            exitSurf=bigfont.render('! GAME OVER ! your score = ' + str(int(score)),1,Red)         # Displaying Game Over when bomb hits the hero
            exitRect= exitSurf.get_rect()
            exitRect.center=(250,200)
            screen.blit(exitSurf, exitRect)
            flag=False
        elif bombx==herox+i and bomby==(heroy-45):
            exitSurf=bigfont.render('! GAME OVER ! your score = ' + str(int(score)),1,Red)
            exitRect= exitSurf.get_rect()
            exitRect.center=(250,200)
            screen.blit(exitSurf, exitRect)
            flag=False
    pygame.display.update()
    Clock.tick(FPS)

    
    if flag==False:
        newgSurf=BASICFONT.render('To start game again press space , to quit press Q',1,Green)      # Play again or not    
        newgRect= newgSurf.get_rect()
        newgRect.center=(250,220)
        screen.blit(newgSurf, newgRect)
        for event in pygame.event.get():                 
            if event.type == KEYUP:
                if event.key == K_Q:                    # Quit the game                
                    flag=False
                    pygame.quit()
                    sys.exit()
                    pygame.display.update()
                    break
                elif event.key == K_SPACE:              # Restart the game
                    herox = 0
                    heroy = 300
                    bomby=-50
                    score=0
                    flag=True
                    pygame.display.update()
    continue
    pygame.display.update()

    
for event in pygame.event.get():          # Manually quitting game by killing the program to run
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
pygame.display.update()
Clock.tick(FPS)



