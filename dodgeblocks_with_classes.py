import pygame,sys
from pygame.locals import *
import os
import random
from itertools import cycle


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
    def colliding(self, enemy):
        xvals = self.x+self.width
        yvals = self.y+self.height

class Enemy:
    key = 0
    x = 0
    y = 0
    width = 0
    height = 0
    right = False
    left = False
    up = False
    down = False
    speed = 0
    def __init__(self, key):
        self.key = key
        self.speed = random.randint(1,5)
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






black = (0,0,0)
red = (255,0,0)
grey = (150,150,150)
white = (0,0,0)
blue = (0,0,255)

displayx = 1080
displayy = 500

round = 1


def sprite(x, y, width, height, DISPLAY):
    pygame.draw.rect(DISPLAY, black, (x, y, width, height))
    pygame.draw.rect(DISPLAY, blue, (x + 5, y + 5, width - 5, height - 5))
def sprite2(x, y, width, height, DISPLAY):
    pygame.draw.rect(DISPLAY, black, (x, y, width, height))




#game loop
running = True
killed = False
clock = pygame.time.Clock()


p=Player(displayx,displayy,25,25,1,False,False,True,False)
e=[Enemy(0),Enemy(1),Enemy(2),Enemy(3)]
while running:
    pygame.init()
    pygame.font.init()
    clock.tick(48)  # 48 is normval
    font = pygame.font.Font('freesansbold.ttf', 32)

    DISPLAY = pygame.display.set_mode((displayx, displayy))
    pygame.display.set_caption("tests")
    DISPLAY.fill(grey)
    sprite(p.x, p.y, p.width, p.height, DISPLAY)
    for enemy in e:
        sprite2(enemy.x, enemy.y, enemy.width, enemy.height, DISPLAY)
    # create bounds for player

    if not killed:
        text = font.render(str(round), True, red)
        text2 = font.render("", True, red)
        round += 1
        if round % int(1000 / len(e)) == 0 and len(e) < 25:
            e.append(Enemy(len(e)))
            if p.speed < 3:
                p.speed += 1



    else:
        p.speed = 0
        for enemy in e:
            enemy.speed = 0
        text = font.render("GAME OVER", True, red)
        text2 = font.render("Press Space to Restart", True, red)

    textRect = text.get_rect()
    textRect.center = (displayx // 2, displayy // 2)
    text2Rect = text2.get_rect()
    text2Rect.center = (displayx // 2, displayy // 2 + 40)
    DISPLAY.blit(text, textRect)
    DISPLAY.blit(text2, text2Rect)

    # display
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
            #pygame.quit()

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
        elif event.key == pygame.K_SPACE:
            running = True
            killed = False
            for enemy in e:
                del(enemy)
            e.append(Enemy(0))
            p.y = displayy/2
            p.x = displayx/2
            print (p.x)
            print(p.y)
            p.speed = 1


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


    for enemy in e:
        if (enemy.x < p.x + p.width) and (enemy.x + enemy.width > p.x) and (enemy.y < p.y + p.height) and (enemy.y + enemy.height > p.y):
            killed = True
    for enemy in e:
        if (enemy.x < p.x + p.width) and (enemy.x + enemy.width > p.x) and (enemy.y < p.y + p.height) and (enemy.y + enemy.height > p.y):
            killed = True


