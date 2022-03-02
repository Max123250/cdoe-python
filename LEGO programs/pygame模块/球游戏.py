import pygame,random,time
def check_collision():
    global  x,y,x_2,y_2,x_speed,y_speed,x_2_speed,y_2_speed,score
    if (0 <= x_2 - x <= 80 or 0 <= x - x_2 <= 80) and (0 <= y_2 - y <= 80 or 0 <= y - y_2 <= 80):
        x_speed = -x_speed
        y_speed = -y_speed
        x_2_speed = -x_2_speed
        y_2_speed = -y_2_speed
        score += 1
        print(score)
def check_collision_ground(y):
    global life
    if y >= 520:
        life -= 1
        if life == 0:
            return False
        
    return True
x = random.randint(0,720)
y = 0
x_2 = 720
y_2 = 520
x_speed = 5
y_speed = 5
x_2_speed = 0
y_2_speed = 0
score = 0
life = 1
a = []
score_list = []
pygame.init()
s = pygame.display.set_mode([800,600])
s.fill([255,255,255])
ball = pygame.image.load("排球.png")
ball2 = pygame.image.load("排球.png")
game_file = open("球游戏存档.txt","r+")
game = game_file.readlines()
for i in range(len(game)):
    a = game[i].split(",")
    print(a[1])
    a[1].strip('\n')
    score_list.append(int(a[1]))
    print(a[1])

run = True
while run:
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

    
    check_collision()
    run = check_collision_ground(y)

    font = pygame.font.Font(None,100)
    f = font.render(str(score),1,(0,0,0))
    f2 = font.render(str(life),1,(0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEMOTION:
            x_2 = event.pos[0] - 30
            y_2 = 520

    s.fill([255,255,255])
    s.blit(ball,[x,y])
    s.blit(ball2,[x_2,y_2])
    s.blit(f,[10,10])
    s.blit(f2,[760,10])
    pygame.display.flip()
    pygame.time.delay(10)
run = True
while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    if score <= int(min(score_list)):
        f3 = font.render("LLLLLLLLLLLLLLLL",1,(0,0,0))
    elif score >= int(max(score_list)):
        f3 = font.render("o7o7o7o7o7o7o7",1,(0,0,0))
    else:
        f3 = font.render("nothing",1,(0,0,0))
    pos = f3.get_witch()
    s.fill([255,255,255])
    s.blit(f3,[400 - pos[0],300 - pos[1]])
    pygame.display.flip()
time = time.strftime("%Y-%m-%d %H-%M-%S" + ",")
game_file.write(time + str(score) + "\n")
game_file.close()
pygame.quit()







