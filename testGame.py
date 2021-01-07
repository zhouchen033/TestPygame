import pygame
import random

pygame.init()
Width = 600
Height = 400
screen = pygame.display.set_mode([Width,Height])
clock = pygame.time.Clock()

def drawCircle(size,color,pos):
    pygame.draw.circle(screen,color,pos,size)

def showMessage(text,size,color,pos):
    font = pygame.font.Font(None,size)
    surface = font.render(text,True,color)
    screen.blit(surface,pos)

running = True
counter = 0
s = 0
while running:
    s += 1
    if s >= 10:
        counter += 1
        s = 0
    screen.fill([0,0,0])
    showMessage("Time:" + str(counter),50,[255,0,0],[250,150])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(10)
    pygame.display.flip()
pygame.quit()



