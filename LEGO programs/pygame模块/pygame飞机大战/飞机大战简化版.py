import pygame
pygame.init()
s = pygame.display.set_mode([480,700])
s.fill([255,255,255])
bg = pygame.image.load("image/background.png")
u_plane = pygame.image.load("image/u_plane.png")
bullet = pygame.image.load("image/bullet.png")
u_x = 0
u_y = 0
b_x = 270
b_y = 700
bullet_bool = False
frist_bullet_bool = False
run = True

while run:
    s.blit(bg,[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEMOTION:
            u_x = event.pos[0] - 40
            u_y = event.pos[1] - 40
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet_bool = True
            frist_bullet_bool = True
    if bullet_bool:
        b_x = u_x + 38
        if frist_bullet_bool:
            b_y = u_y
            frist_bullet_bool = False
        b_y -= 10
        s.blit(bullet,[b_x,b_y])
        if b_y <= 0:
            bullet_bool = False
            b_y = 700
    s.blit(u_plane,[u_x,u_y])
    pygame.display.flip()
    pygame.time.delay(10)
pygame.quit()
