import turtle as t
t.screensize(1000,1000,'white')
#t.shape('turtle')

#t.speed(1)
# 往下移动
t.up()
t.goto(0,-120)
t.down()

#画菱形函数
def diamond():
    t.fillcolor('yellow')
    t.pencolor('black')
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.rt(60)
        t.fd(80)
        t.rt(120)
    t.end_fill()
    
#1.画圆
t.pencolor('red')
t.circle(120,360)

#2.画菱形
t.rt(60)
for i in range(12):
    diamond()
    t.rt(30)
    t.penup()
    t.goto(0,0)# 去到圆心
    t.rt(30)
    t.fd(120)
    t.lt(30)
    t.pendown()




    
