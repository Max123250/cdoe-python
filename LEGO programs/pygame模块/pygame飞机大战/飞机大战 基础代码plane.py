import pygame
import random

# 初始化
pygame.init()
# 创建一个窗口
screen_w = 480
screen_h = 650
screen = pygame.display.set_mode([screen_w,screen_h])
pygame.display.set_caption("飞机大战 v0.9")
#背景图
bg = pygame.image.load("plane/images/bg.png")

# 循环播放背景音乐
pygame.mixer.music.load("plane/sound/game_music.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

screen.blit(bg,[0,0])
pygame.display.flip()



# 时钟
clock = pygame.time.Clock()

running = True
while running:
    #控制帧速率
    clock.tick(30)
    
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.delay(10)
    
pygame.quit()
