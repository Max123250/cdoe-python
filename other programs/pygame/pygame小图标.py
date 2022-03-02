import pygame
pygame.init()
s=pygame.display.set_mode([640,480])
s.fill([255,255,255])
pygame.draw.circle(s,[255,0,0],[320,200],30,5)
pygame.draw.rect(s,[255,0,0],[286,240,68,10],0)
pygame.draw.rect(s,[255,0,0],[316,228,10,80],0)
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()
