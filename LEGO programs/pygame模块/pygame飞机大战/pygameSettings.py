'''
本文件由Max制作
为pygame游戏的额外设置
'''
import pygame


def error(name):
    raise ValueError(name)


class Game():

    class Mouse():
        def __init__(self):
            self.down = False


    def __init__(self,background = ""):
        self.score = 0
        if background != "":
            self.bg = pygame.image.load(background)

    def blit(self,img,pos):
        x = pos[0]
        y = pos[1]
        s.blit(img,[x,y])

    def blit_background(self):
        if self.bg != "":
            self.blit(self.bg,[0,0])
        else:
            error("no background in.you can't display the background before you enter it.")

    def blitRGB(self,RGB):
        r = RGB[0]
        g = RGB[1]
        b = RGB[2]
        s.fill([r,g,b])

    def flip(self):
        pygame.display.flip()

    def set_delay(self,time):
        pygame.time.delay(time)

    def set_caption(self,name):
        pygame.display.set_caption(name)

    def blit_score(self,score):
        font = pygame.font.Font(None,100)
        f = font.render(str(score),1,[0,0,0])
        s.blit(f,[10,10])


def init(screen = [640,480]):
    x = screen[0]
    y = screen[1]
    pygame.init()
    s = pygame.display.set_mode([x,y])
    game = Game()
    game.mouse = game.Mouse()
