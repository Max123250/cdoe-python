'''
碰撞检测：
if (0 <= x1 - x2 <= w2 or 0 <= x2 - x1 <= w1)\
 and (0 <= y1 - y2 <= y2 or 0 <= y2 - y1 <= y1):
    return True
'''
import pygame,random

def check(x1,y1,w1,h1,x2,y2,w2,h2):
    '''
    if (0 <= x1 - x2 <= w2 or 0 <= x2 - x1 <= w1) \
     and (0 <= y1 - y2 <= h2 or 0 <= y2 - y1 <= h1):
        return True
    '''
    if (0 <= x1 - x2<= w2) and (0 <= y1 - y2 <= h2 or 0 <= y2 - y1 <= h1):
        return True
    elif (0 <= x2 - x1 <= w1) and (0 <= y1 - y2 <= h2 or 0 <= y2 - y1 <= h1):
        return True
    else:
        return False


class UPlane():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 80
        self.h = 80
        self.pos = [self.x,self.y]
        self.image = pygame.image.load("image/u_plane.png")

    def blit(self):
        s.blit(self.image,self.pos)


class APlane():
    def __init__(self):
        self.x = random.randint(0,400)
        self.y = 0
        self.w = 80
        self.h = 80
        self.pos = [self.x,self.y]
        self.speed = 5
        self.images = [  pygame.image.load("image/a_plane.png")
                       ,pygame.image.load("image/a_plane_d1.png")
                       ,pygame.image.load("image/a_plane_d2.png")
                       ,pygame.image.load("image/a_plane_d3.png")]
        self.image = self.images[0]
        self.image_while_times = 0
        self.image_index = 1
        self.die = False
        self.hit = False
        self.broken_time = 0
        self.check_srore = True

    def move(self):
        if self.hit:
            if self.image_index > 3:
                self.die = True
                self.image_index = 0
            else:
                self.image = self.images[self.image_index]
                self.image_while_times += 1
                if self.image_while_times == 5:
                    self.image_while_times = 0
                    self.image_index += 1
        if self.die:
            self.x = random.randint(0,400)
            self.y = random.randint(-700,-80)
            self.y += self.speed
            self.die = False
            self.hit = False
            self.image = self.images[0]
        else:
            self.y += self.speed

    def check_boom(self):
        if self.y >= 700:
            self.kill()
            self.y = random.randint(-700,-80)
            game.score -= 1

    def kill(self):
        self.hit = True
        self.move()

    def blit(self):
        s.blit(self.image,[self.x,self.y])

    def check_atk(self,x,y,w,h):
        if_check = check(self.x,self.y,self.w,self.h,x,y,w,h)
        if if_check and not self.hit:
            self.kill()
            game.score -= 2

    def broken(self,time):
        if time == 1:
            self.image = self.images[1]
        elif time == 2:
            self.image = self.images[2]
        elif time == 3:
            self.image = self.images[3]
        else:
            self.image = self.images[0]


class Game():
    def __init__(self):
        self.image = pygame.image.load("image/background.png")
        self.mouse_down = False
        self.space_down = False
        self.last_space_event = False
        self.score = 0
        self.timer = pygame.USEREVENT
        self.meny_timer = 1
        self.mouse_pos = [0,0]
        self.key_s_down = False

    def blit_screen(self):
        s.blit(self.image,[0,0])

    def fill_white(self):
        s.fill([255,255,255])

    def flip(self):
        pygame.display.flip()

    def delay(self,t):
        pygame.time.delay(t)

    def set_caption(self,cap):
        pygame.display.set_caption(cap)

    def blit_score(self):
        font = pygame.font.Font(None,50)
        f = font.render(str(self.score),1,[0,0,0])
        s.blit(f,[10,10])

    def set_timer(self):
        pygame.time.set_timer(self.timer,20000)

    def check_last_space(self):
        last = []
        last.append(self.space_down)
        self.last_space_event = last[0]


class Bullet():
    def __init__(self,x,y):
        self.image = pygame.image.load("image/bullet.png")
        self.x = x
        self.y = y
        self.w = 5
        self.h = 11
        self.pos = [self.x,self.y]
        self.launch = False
        self.speed = 5

    def launch_a(self,x,y,first):
        if first:
            self.x = x + 38
            self.y = y
            self.launch = True
        else:
            self.y -= self.speed
        if self.y <= 10:
            self.launch = False

    def blit(self):
        s.blit(self.image,[self.x,self.y])

    def check_atk(self,a_planes):
        if self.launch:
            for i in range(5):
                a_plane = a_planes[i]
                if_check = check(self.x,self.y,self.w,self.h,a_plane.x,a_plane.y,a_plane.w,a_plane.h)
                if if_check:
                    a_plane.kill()
                    self.kill()
                    game.score += 5

    def kill(self):
        self.y = 10
        self.launch = False


class BombSubbly():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 60
        self.h = 107
        self.x_speed = 4.5
        self.y_speed = 1.5
        self.flyying = False
        self.image = pygame.image.load("image/bomb_supply.png")
        self.get = False

    def move(self,first):
        if first:
            self.x = random.randint(0,420)
            self.y = random.randint(-300,-107)
            self.x += self.x_speed
            self.y += self.y_speed
            self.flyying = True
            self.get = False
        else:
            self.x += self.x_speed
            self.y += self.y_speed
            if self.x <= 0:
                self.x_speed = -self.x_speed
            if self.x >= 420:
                self.x_speed = -self.x_speed

    def blit(self):
        if self.flyying:
            s.blit(self.image,[self.x,self.y])

    def check_broken(self):
        broken = check(self.x,self.y,self.w,self.h\
                      ,u_plane.x,u_plane.y,u_plane.w,u_plane.h)
        if broken:
            self.flyying = False
            self.get = True
        else:
            self.get = False

    def boom(self,a_planes):
        if not game.last_space_event == game.space_down:
            if l_bomb.much >= 1:
                if game.space_down:
                    l_bomb.much -= 1
                    for i in range(len(a_planes)):
                        a_plane = a_planes[i]
                        if a_plane.y + 80 >= 0:
                            a_plane.kill()
                            game.score += 1
        game.space_down = False


class LittleBomb():
    def __init__(self):
        self.x = 360
        self.y = 1
        self.much = 99
        self.image = pygame.image.load("image/bomb.png")

    def set_meny(self):
        font = pygame.font.Font(None,50)
        f = font.render("X" + str(self.much),1,[0,0,0])
        s.blit(f,[430,10])

    def check_new_bomb(self,new):
        if new:
            self.much += 1
            bomb.get = False

    def blit(self):
        s.blit(self.image,[self.x,self.y])


class Stop():
    def __init__(self):
        self.images = [pygame.image.load("image/pause_pressed.png")
                    ,pygame.image.load("image/resume_pressed.png")]
        self.image = self.images[0]
        self.x = 210
        self.y = 45
        self.w = 60
        self.h = 45

    def check(self):
        if game.key_s_down:
            self.image = self.images[1]
        else:
            self.image = self.images[0]

    def blit(self):
        s.blit(self.image,[210,0])


pygame.init()
game = Game()
bomb = BombSubbly()
l_bomb = LittleBomb()
stop = Stop()
u_plane = UPlane(200,450)
s = pygame.display.set_mode([480,700])
game.set_caption("肥鸡打站")
game.set_timer()

while_times = 0

bullets=[]
for i in range(20):
    bullet = Bullet(0,0)
    bullets.append(bullet)

a_planes = []
for i in range(5):
    a_plane = APlane()
    a_planes.append(a_plane)


run = True
while run:
    if not game.key_s_down:
        game.blit_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEMOTION:
            game.mouse_pos = [event.pos[0],event.pos[1]]
            u_plane.pos[0] = event.pos[0] - 40
            u_plane.pos[1] = event.pos[1] - 40

        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.mouse_down = True

        elif event.type == pygame.MOUSEBUTTONUP:
            game.mouse_down = False

        elif event.type == game.timer:
            bomb.move(True)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.space_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                game.space_down = False
            if event.key == pygame.K_s:
                game.key_s_down = not game.key_s_down

    stop.check()
    stop.blit()
    if game.key_s_down:
        pygame.display.flip()
        continue

    if game.mouse_down:
        if while_times == 5:
            for i in range(10):
                if not bullets[i].launch:
                    bullets[i].launch = True
                    bullets[i].launch_a(u_plane.pos[0],u_plane.pos[1],True)
                    break


    for i in range(len(bullets)):
        bullets[i].check_atk(a_planes)
        if bullets[i].launch:
            bullets[i].launch_a(bullets[i].x,bullets[i].y,False)
            s.blit(bullets[i].image,[bullets[i].x,bullets[i].y])


    for i in range(len(a_planes)):
        a_planes[i].check_boom()
        a_planes[i].check_atk(u_plane.x,u_plane.y,u_plane.w,u_plane.h)
        a_planes[i].move()


    if while_times == 5:
        while_times = 0
    else:
        while_times += 1

    u_plane.x = u_plane.pos[0]
    u_plane.y = u_plane.pos[1]

    l_bomb.check_new_bomb(bomb.get)
    l_bomb.set_meny()

    if bomb.flyying:
        bomb.move(False)
        bomb.blit()
        bomb.check_broken()
    bomb.boom(a_planes)

    l_bomb.blit()

    u_plane.blit()
    for i in range(5):
        a_planes[i].blit()

    game.blit_score()
    game.flip()
    game.delay(10)
    game.check_last_space()


pygame.quit()