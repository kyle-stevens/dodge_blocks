import pygame,sys
from pygame.locals import *
import os
import random



class Player:
    x=0
    y=0
    height=0
    width=0
    speed=0
    right=False
    left=False
    up=True
    down=False
    def __init__(self, x,y,height,width,speed,right,left,up,down ):
        self.x = x *0.5
        self.y = y *0.5
        self.height = height
        self.width = width
        self.speed = speed
        self.right = right
        self.left = left
        self.up = up
        self.down = down

class Enemy:
    x = 0
    y = 0
    width = 0
    height = 0
    right = False
    left = False
    up = False
    down = False
    speed = 0
    def __init__(self):
        self.speed = 1#random.randint(1,10)
        self.x = random.randint(0,700)
        self.y = 0
        self.width = 10
        self.height = 10
        self.down = True
        rightorleft = random.randint(0,2)
        if rightorleft == 0:
            self.right = True
        else:
            self.left = True

    def collision(self, other):
        if self.x == (other.x) or (self.x ) == other.x:
            tempright = self.right
            templeft = self.left
            self.right = other.right
            self.left = other.left
            other.right = tempright
            other.left = templeft

        elif self.y == (other.y) or (self.y)==other.y:
            tempup = self.up
            tempdown = self.down
            self.up = other.up
            self.down = other.down
            other.up = tempup
            other.down = tempdown





black = (0,0,0)
red = (255,0,0)
grey = (150,150,150)
white = (0,0,0)

displayx = 1080
displayy = 500

round = 1


def sprite(x, y, width, height, DISPLAY):
    pygame.draw.rect(DISPLAY, black, (x, y, width, height))
    pygame.draw.rect(DISPLAY, red, (x + 5, y + 5, width - 5, height - 5))
def sprite2(x, y, width, height, DISPLAY):
    pygame.draw.rect(DISPLAY, black, (x, y, width, height))




#game loop
running = True
clock = pygame.time.Clock()


p=Player(displayx,displayy,25,25,1,False,False,True,False)
e=[Enemy()]
while running:
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(round), True, black)
    round+=1
    textRect = text.get_rect()
    textRect.center = (displayx // 2, displayy // 2)
    if round % int(1000/len(e)) ==0 and len(e) < 25:
        e.append(Enemy())
        if p.speed < 3:
            p.speed += 1



    # display
    DISPLAY = pygame.display.set_mode((displayx, displayy))
    pygame.display.set_caption("tests")
    DISPLAY.fill(grey)
    DISPLAY.blit(text, textRect)
    sprite(p.x, p.y, p.width, p.height, DISPLAY)
    for enemy in e:
        sprite2(enemy.x,enemy.y,enemy.width,enemy.height,DISPLAY)
    #create bounds for player
    if p.x > (displayx - (p.width)):
        # to create boundaries
        p.right = False
        p.left = True
    elif p.x < 0:
        # to create boundaries
        p.left = False
        p.right = True
    if p.y > (displayy - p.height):
        # to create boundaries
        p.down = False
        p.up = True
    elif p.y < 0:
        # to create boundaries
        p.up = False
        p.down = True


    #commands
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
    if event.type == pygame.KEYDOWN:
        '''if event.key == pygame.K_RIGHT and p.right:
            p.right = False
        elif event.key == pygame.K_LEFT and p.left:
            p.left = False
        elif event.key == pygame.K_DOWN and p.down:
            p.down = False
        elif event.key == pygame.K_UP and p.up:
            p.up = False'''
        if event.key == pygame.K_LEFT:
            p.right = False
            p.left = True
        elif event.key == pygame.K_RIGHT:
            p.left = False
            p.right = True
        elif event.key == pygame.K_UP:
            p.down = False
            p.up = True
        elif event.key == pygame.K_DOWN:
            p.up = False
            p.down = True

    #handle motion
    if p.left and p.up:
        p.x = p.x-p.speed
        p.y = p.y-p.speed
    elif p.left and p.down:
        p.x = p.x - p.speed
        p.y = p.y + p.speed
    elif p.right and p.up:
        p.x = p.x + p.speed
        p.y = p.y - p.speed
    elif p.right and p.down:
        p.x = p.x + p.speed
        p.y = p.y + p.speed
    elif p.left:
        p.x = p.x-p.speed
    elif p.right:
        p.x = p.x+p.speed
    elif p.up:
        p.y = p.y-p.speed
    elif p.down:
        p.y = p.y+p.speed


    for elem in e:
        thiselem = elem
        nextelem = e[e.index(elem) - len(e) + 1]
        thiselem.collision(nextelem)
        #taken from ignoramus on stack overflow

    for enemy in e:

        #create bounds for enemies
        if enemy.x > (displayx - (enemy.width)):
            # to create boundaries
            enemy.right = False
            enemy.left = True
        elif enemy.x < 0:
            # to create boundaries
            enemy.left = False
            enemy.right = True
        if enemy.y > (displayy - enemy.height):
            # to create boundaries
            enemy.down = False
            enemy.up = True
        elif enemy.y < 0:
            # to create boundaries
            enemy.up = False
            enemy.down = True
    
        #enemymotion
        if enemy.left and enemy.up:
            enemy.x = enemy.x-enemy.speed
            enemy.y = enemy.y-enemy.speed
        elif enemy.left and enemy.down:
            enemy.x = enemy.x - enemy.speed
            enemy.y = enemy.y + enemy.speed
        elif enemy.right and enemy.up:
            enemy.x = enemy.x + enemy.speed
            enemy.y = enemy.y - enemy.speed
        elif enemy.right and enemy.down:
            enemy.x = enemy.x + enemy.speed
            enemy.y = enemy.y + enemy.speed
        elif enemy.left:
            enemy.x = enemy.x-enemy.speed
        elif enemy.right:
            enemy.x = enemy.x+enemy.speed
        elif enemy.up:
            enemy.y = enemy.y-enemy.speed
        elif enemy.down:
            enemy.y = enemy.y+enemy.speed
    

    #pygame.time.delay(1)
    pygame.display.update()
    clock.tick(48)
'''needs work for collision detection
    for enemy in e:
        if enemy.x < (p.x+25):
            if enemy.x > p.x:
                if enemy.y < (p.y+25):
                    if enemy.y< p.y:
                        text = font.render("Game Over", True, red)
                        textRect = text.get_rect()
                        textRect.center = (displayx // 2, displayy // 2)
                        pygame.time.delay(10)
'''
