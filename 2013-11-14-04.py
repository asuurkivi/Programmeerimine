import pygame, sys
pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.circle(screen,[255,0,0],[250,250],100,0)
pygame.draw.circle(screen,[0,255,0],[330,250],100,0)
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
