import pygame
pygame.init()
s = pygame.display.set_mode([800,600])
s.fill([255,255,255])
ball = pygame.image.load("排球.png")
ball2 = pygame.image.load("排球.png")
x = 0
y = 0
x_2 = 720
y_2 = 520
x_speed = 0
y_speed = 0
x_2_speed = 0
y_2_speed = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_2 += 10
            elif event.key == pygame.K_UP:
                y_2 -= 10
            elif event.key == pygame.K_LEFT:
                x_2 -= 10
            elif event.key == pygame.K_RIGHT:
                x_2 += 10
        elif event.type == pygame.MOUSEMOTION:
            x = event.pos[0] - 40
            y = event.pos[1] - 40
    x += x_speed
    y += y_speed
    x_2 += x_2_speed
    y_2 += y_2_speed
    if x >= 720 or x <= 0:
        x_speed = -x_speed
    if y >= 520 or y <= 0:
        y_speed = -y_speed
    if x_2 >= 720 or x_2 <= 0:
        x_2_speed = -x_2_speed
    if y_2 >= 520 or y_2 <= 0:
        y_2_speed = -y_2_speed
    s.fill([255,255,255])
    s.blit(ball,[x,y])
    s.blit(ball,[x,y])
    pygame.display.flip()
    pygame.time.delay(10)
pygame.quit()






