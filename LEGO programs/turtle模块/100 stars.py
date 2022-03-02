import turtle as tp
import random
tp.screensize(800,600,"black")
tp.shape("turtle")
tp.pensize(2)

tp.speed(11)
tp.hideturtle()
def print_star(x,y,size,color):
    tp.pencolor(color)
    tp.fillcolor(color)
    tp.penup()
    tp.goto(x,y)
    tp.pendown()
    tp.begin_fill()
    for i in range(5):
        tp.fd(size)
        tp.rt(144)
    tp.end_fill()
turn=0
while turn<=100:
    x=random.randint(-400,400)
    y=random.randint(-300,300)
    size=random.randint(50,100)
    focolor=["red","green","blue","yellow","white","orange"]
    color=random.choice(focolor)
    turn=turn+1
    print_star(x,y,size,color)
