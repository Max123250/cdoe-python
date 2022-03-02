import turtle as t
t.screensize(800,600,"white")
t.speed(5)
#t.ht()
'''
t.penup()
t.goto(0,300)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.rt(120)
t.fd(300)
for i in range(2):
    t.lt(120)
    t.fd(300)
'''
# 圆    
t.penup()
t.goto(-150,-300)
t.pendown()
t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
t.rt(90)
t.circle(150,-180)
t.end_fill()

# 三角
t.penup()
t.goto(150,-150)
t.pendown()
t.pencolor("red")
t.fillcolor("yellow")
t.lt(30)
t.begin_fill()
for i in range(3): 
    t.fd(300)
    t.lt(120)
t.end_fill()
t.ht()
