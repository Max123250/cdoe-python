class Ball:
    def __init__(self,color,size,where):
        self.color = color
        self.size = size
        self.where = where
    def move(self):
        global x,y
        if self.where == "up":
            y = y + 5
        if self.where == "down":
            y = y - 5
        if self.where == "left":
            x = x - 5
        if self.where == "right":
            x = x + 5
        else:
            pass
x = 0
y = 0
color = input("The color of the ball is:")
size = input("The size of the ball is:")
where = input("Enter where:(up/down/left/right)")
while True:
    change = input("change:(color/size/where/no)")
    if change == "color":
        color = input("Enter the color:")
        print("color =",color)
    elif change == "size":
        size = input("Enter the size:")
        print("size =",size)
    elif change == "where":
        where = input("Enter where:")
        print("where =",where)
    else:
        pass
    ball = Ball(color,size,where)
    ball.move()
    print("ball:\t"
          ,"x = ",x,"\t"
          ,"y = ",y,"\t"
          ,"color = ",ball.color,"\t"
          ,"size = ",ball.size)
