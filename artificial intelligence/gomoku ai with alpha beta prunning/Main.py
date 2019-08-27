import pygame
import Alpha_beta_Search
from State import State

from pygame.locals import *

pygame.init()
width, height = 600, 600
screen=pygame.display.set_mode((width, height))


def findxy(pos):
    x = 0
    y = 0
    minx = 10000
    miny = 10000
    for i in range(1, 20):
        tempx = abs(pos[0] - i*30)
        if tempx < minx:
            minx = tempx
            x = i
    for i in range(1, 20):
        tempy = abs(pos[1] - i*30)
        if tempy < miny:
            miny = tempy
            y = i
    return (x, y)


running = 1
exitcode = 0
state = State()
turn = 1
vpos = (0, 0)
vposs = []
vposs2 = []
click = 0
while running:
    screen.fill((200, 200, 200))
    for i in range(1, 20):
        pygame.draw.line(screen, (0 ,0, 0), (i*30, 30), (i*30, 570), 1)
        pygame.draw.line(screen, (0, 0, 0), (30, i*30), (570, i*30), 1)
        pygame.draw.circle(screen, (0, 0, 0), (300, 300), 4, 0)
        pygame.draw.circle(screen, (0, 0, 0), (120, 120), 4, 0)
        pygame.draw.circle(screen, (0, 0, 0), (120, 300), 4, 0)
        pygame.draw.circle(screen, (0, 0, 0), (120, 480), 4, 0)
        pygame.draw.circle(screen, (0, 0, 0), (300, 120), 4, 0)
        pygame.draw.circle(screen, (0, 0, 0), (300, 480), 4, 0)
        pygame.draw.circle(screen, (0, 0, 0), (480, 120), 4, 0)
        pygame.draw.circle(screen, (0, 0, 0), (480, 300), 4, 0)
        pygame.draw.circle(screen, (0, 0, 0), (480, 480), 4, 0)
    if click == 1 and turn == 1:
        position=pygame.mouse.get_pos()
        position1 = findxy(position)
        vposs.append((position1[0]*30, position1[1]*30))
        Alpha_beta_Search.update(state, position1[0]-1, position1[1]-1, 1)
        click = 0
        turn = 2
    for vpos in vposs:
        pygame.draw.circle(screen, (0, 0, 0), vpos, 10, 0)
    for vpos in vposs2:
        pygame.draw.circle(screen, (255, 255, 255), vpos, 10, 0)
    pygame.display.flip()
    if turn == 2:
        compos = Alpha_beta_Search.alphaBetaSearch(state)
        Alpha_beta_Search.update(state, compos[0], compos[1], 2)
        vposs2.append(((compos[0] + 1)*30, (compos[1] + 1)*30))
        turn = 1
    for vpos in vposs2:
        pygame.draw.circle(screen, (255, 255, 255), vpos, 10, 0)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type==pygame.MOUSEBUTTONDOWN:
            click = 1

if exitcode==0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == MOUSEBUTTONDOWN:
            break
    pygame.display.flip()

