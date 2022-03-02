import turtle as tp
tp.screensize(800,600,"red")
tp.shape("turtle")
tp.pensize(2)
tp.pencolor("yellow")
tp.speed(5)
tp.hideturtle()
def print_star(x,y,size):
    tp.fillcolor("yellow")
    tp.penup()
    tp.goto(x,y)
    tp.pendown()
    tp.begin_fill()
    for i in range(5):
        tp.fd(size)
        tp.rt(144)
    tp.end_fill()
print_star(-500,200,200)
print_star(-250,300,50)
print_star(-200,230,50)
print_star(-200,130,50)
print_star(-250,50,50)
wait = tp.Screen()
wait.exitonclick()




