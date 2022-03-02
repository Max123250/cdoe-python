import turtle  as  t
import random
t.screensize(800,600,"white")
t.pencolor("black")
t.fillcolor("yellow") #填充的颜色
t.pensize(5) # 线宽5

#画星星函数
def drawStar(x,y,l):
    t.up()
    t.goto(x,y)·
    t.down()
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(5):
    t.fd(l)#控制五角星的大小
    t.rt(144)
    t.end_fill()

# for循环画5颗星星
for i in range(5): 
    # 随机生成400到250的数字作为x坐标
    x = random.randint(-400,250)
    # 随机生成-150到10的数字作为y坐标
    y = random.randint(-150,100)
    # 随机生成10到150的数字作为边长，
    l = random.randint(10,150)
    # 画星星
    drawStar(x,y,l)

'''
注：
边长范围是题目要求的，坐标是估算不要让星星超窗口
算不清楚就完成前两小题即可，写完代码一定要运行，
千万不要因为最后一步坐标没写对，导致结果全看不见，
看不见结果得零分！
评分是看结果的，不看中间过程。·
'''





