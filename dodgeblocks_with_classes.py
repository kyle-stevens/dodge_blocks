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


    def __init__(self):
        return




black = (0,0,0)
red = (255,0,0)
grey = (150,150,150)
white = (0,0,0)

displayx = 700
displayy = 700


def sprite(x, y, width, height, DISPLAY):
    pygame.draw.rect(DISPLAY, black, (x, y, width, height))
    pygame.draw.rect(DISPLAY, red, (x + 5, y + 5, width - 5, height - 5))


def game():
    #game loop
    running = True
    clock = pygame.time.Clock()

    p=Player(displayx,displayy,25,25,1,False,False,True,False)
    while running:


        pygame.init()

        # display
        DISPLAY = pygame.display.set_mode((displayx, displayy))
        pygame.display.set_caption("tests")
        DISPLAY.fill(grey)

        sprite(p.x, p.y, p.width, p.height, DISPLAY)

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


        #pygame.time.delay(1)
        pygame.display.update()
        clock.tick(48)

def main():
    game()
    return
if __name__ == "__main__":
    main()