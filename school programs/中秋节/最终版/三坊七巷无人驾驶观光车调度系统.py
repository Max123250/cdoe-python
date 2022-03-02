import time
import pygame
import easygui as gui
class Car():
    def __init__(self):
        self.pos = [20,0]
        self.image = pygame.image.load("car_1.png")
        self.speed_x = 1
        self.speed_y = 0

    def move(self):
        self.pos[0] += self.speed_x
        self.pos[1] += self.speed_y
        if self.pos == [400,0]:
            self.speed_y = 1
        if self.pos == [425,25]:
            self.speed_x = 0
        if self.pos == [425,210]:
            self.speed_x = -2
            self.speed_y = 1
        if self.pos == [395,225]:
            self.speed_y = 0
            self.speed_x = -1
        if self.pos == [40,225]:
            self.speed_y = -1
        if self.pos == [0,185]:
            self.speed_x = 0
        if self.pos == [0,20]:
            self.speed_x = 1
        if self.pos == [20,0]:
            self.speed_y = 0
        #上为移动 下为站点
        if self.pos == [145,0]:
            self.stop(1)
            time.sleep(9)
        elif self.pos == [225,0]:
            self.stop(2)
        elif self.pos == [425,125]:
            time.sleep(9)
        elif self.pos == [425,65]:
            self.stop(3)
            time.sleep(9)
            self.stop(4)
            time.sleep(9)

    def stop(self,num):
        if num == 1:
            sound_1.play()
        elif num == 2:
            sound_2.play()
        elif num == 3:
            sound_3.play()
        elif num == 4:
            sound_4.play()

    def blit(self):
        s.blit(self.image,self.pos)


pygame.init()
pygame.mixer.init()
car1 = Car()
file = open("user information.txt","r+")
sound_1 = pygame.mixer.Sound("1.wav")
sound_2 = pygame.mixer.Sound("2.wav")
sound_3 = pygame.mixer.Sound("3.wav")
sound_4 = pygame.mixer.Sound("4.wav")
run = True
mouse_pos = [0,0]
turn = False
while run:
    if turn == False:
        return_gui = gui.buttonbox("欢迎使用无人驾驶观光车调度系统！","调度系统-登录",["登录","注册"])

        if return_gui == "登录":
            re = gui.multpasswordbox("请输入用户名与密码","调度系统-登录",["用户名","密码"])
            in_file = file.readlines()
            information = []
            l = []
            for x in in_file:
                l.extend(x.strip("\n"))
                if len(l) == 2:
                    information.append(l)
                    l = []
            print(information)
            for x in information:
                print(re)
                if re == x:
                    turn = True
                    print(turn)

        elif return_gui == "注册":
            re = gui.multpasswordbox("请输入用户名与密码","调度系统-注册",["用户名","密码"])
            file.write(re[0] + "\n" + re[1] + "\n")


    else:
        s = pygame.display.set_mode([449,247])
        s.fill([255,255,255])
        bg = pygame.image.load("background.png")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos[0] = event.pos[0]
                mouse_pos[1] = event.pos[1]

        car1.move()

        s.blit(bg,[0,0])
        print(mouse_pos)
        car1.blit()
        pygame.display.flip()
        pygame.time.delay(10)



pygame.quit()
file.close()
