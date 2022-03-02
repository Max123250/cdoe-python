import pygame
pygame.init()
s=pygame.display.set_mode([640,480])
s.fill([255,255,255])
ball=pygame.image.load("排球.png")
s.blit_back_ground()
pygame.display.flip()
pygame.time.delay(2000)
s.blit_back_ground()
pygame.draw.rect(s,[255,255,255],[50,50,90,90],0)
pygame.display.flip()
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
pygame.quit()
