import pygame
pygame.init()
s=pygame.display.set_mode([500,300])
s.fill([255,255,255])
pygame.draw.rect(s,[0,0,0],[0,0,500,100],0)
pygame.draw.rect(s,[255,0,0],[0,100,500,100],0)
pygame.draw.rect(s,[255,255,0],[0,200,500,100],0)
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()
