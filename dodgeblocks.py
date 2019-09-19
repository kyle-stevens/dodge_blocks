import pygame,sys
from pygame.locals import *
import os
x=0
y=0
playerspeed = 1
runningright = False
runningleft = False
width = 50
height = 50
displayx = 1535
displayy = 863
runningup = False
runningdown = False
x = displayx * 0.5
y = displayy * 0.5

def sprite(x, y):
    pygame.draw.rect(DISPLAY, black, (x, y, width, height))
    pygame.draw.rect(DISPLAY, red, (x + 5, y + 5, width - 5, height - 5))


#set running bool
running = True
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)



x = displayx * 0.5
y = displayy * 0.5


while running:
    # initialize pygame
    pygame.init()
    #declare common colors
    black = (0,0,0)
    red = (255,0,0)
    white = (255,255,255)
    grey = (125,125,125)
    # create display and set title
    DISPLAY = pygame.display.set_mode((displayx, displayy))
    pygame.display.set_caption("tests")
    DISPLAY.fill(grey)
    sprite(x, y)
    if x>(displayx-(width)):
        #to create boundaries
        runningright = False
    elif x<0:
        #to create boundaries
        runningleft = False
    if y>(displayy-height):
        #to create boundaries
        runningdown = False
    elif y<0:
        #to create boundaries
        runningup = False
    #commands
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and runningright:
            runningright = False
        elif event.key == pygame.K_RIGHT and runningleft:
            runningleft = False
        elif event.key == pygame.K_UP and runningdown:
            runningdown = False
        elif event.key == pygame.K_DOWN and runningup:
            runningup = False
        elif event.key == pygame.K_LEFT:
            runningleft = True
        elif event.key == pygame.K_RIGHT:
            runningright = True
        elif event.key == pygame.K_UP:
            runningup = True
        elif event.key == pygame.K_DOWN:
            runningdown = True
    if runningleft and runningup:
        x = x-playerspeed
        y = y-playerspeed
    elif runningleft and runningdown:
        x = x - playerspeed
        y = y + playerspeed
    elif runningright and runningup:
        x = x + playerspeed
        y = y - playerspeed
    elif runningright and runningdown:
        x = x + playerspeed
        y = y + playerspeed
    elif runningleft:
        x = x-playerspeed
    elif runningright:
        x = x+playerspeed
    elif runningup:
        y = y-playerspeed
    elif runningdown:
        y = y+playerspeed





    pygame.time.delay(1)
    pygame.display.update()