import pygame,random

def imblit(image,x,y):
    s.blit_back_ground()
def alb(l_time):
    global a_plane
    time = int(l_time)
    if time == 1:
        a_plane = pygame.image.load("image/a_plane_d1.png")
    elif time == 2:
        a_plane = pygame.image.load("image/a_plane_d2.png")
    elif time == 3:
        a_plane = pygame.image.load("image/a_plane_d3.png")
    else:
        a_plane = pygame.image.load("image/a_plane.png")

pygame.init()
s = pygame.display.set_mode([450,600])
s.fill([255,255,255])
u_plane = pygame.image.load("image/u_plane.png")
a_plane = pygame.image.load("image/a_plane.png")
bullet = pygame.image.load("image/bullet.png")
u_x = 0
u_y = 0
a_x = 0
a_y = 0
bullet_x = 0
a_speed = 5
a_broken = False
a_broken_time = 1

run = True
while run:
    #事件检测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEMOTION:
            u_x = event.pos[0] - 20
            u_y = 430
    #定义变量
    bullet_x = u_x + 38
    #敌机飞行位置设置
    if a_y == 0:
        a_x = random.randint(70,380)
    a_y += a_speed
    if a_y == 450:
        a_y = 0
    #攻击检测

    if 0 <= 110 - a_y <= 80 and (0 <= a_x - bullet_x <= 6 or 0 <= bullet_x - a_x <= 6):
        a_broken = True


    s.fill([255,255,255])
    imblit(u_plane,u_x,u_y)
    if not a_broken:
        alb(0)
        imblit(a_plane,a_x,a_y)
    else:
        if a_broken_time == 1:
            alb(1)
            imblit(a_plane,a_x,a_y)
        elif a_broken_time == 2:
            alb(2)
            imblit(a_plane,a_x,a_y)
        elif a_broken_time == 3:
            alb(3)
            imblit(a_plane,a_x,a_y)
            a_broken = False
        else:
            alb(0)
            a_y = 0
            imblit(a_plane,a_x,a_y)
    imblit(bullet,bullet_x,110)
    pygame.display.flip()
    pygame.time.delay(10)
pygame.quit()
