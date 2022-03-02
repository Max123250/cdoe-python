# 海龟画图类型(必出)
# 一般头两小题不难，根据要求先完成基础图形
# 掌握基础方法，想象自己在图上作画
# 涉及到超纲的几何知识可以选择性放弃

import turtle as t
# 以下是基础设置，根据题目要求设置
# 题目无要求就不用写
t.screensize(800,800,"white")#画布窗口宽高，底色
t.speed(7) # 画笔速度
t.pensize(1)# 画笔粗细

# 1.画三角
t.pencolor("red") # 画笔颜色
t.fillcolor("yellow")# 填充颜色
t.begin_fill() # 开始填充颜色
# 画具体的图形
for i in range(3):
    t.fd(300) # 画笔前进
    t.lt(120) # 画笔左转，右转是rt
t.end_fill() # 结束填充颜色

# 2.移动坐标，画多幅图形时，笔要先抬起，
# 找到下一个图形的起始位置再落笔
t.penup() # 笔抬起
t.goto(0,-150) # 窗口的中心的原点(0,0)
t.pendown() # 笔落下

# 3.画圆，圆默认是逆时针画出
t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
t.fd(300)
t.lt(90)
t.circle(150,180)
t.end_fill()

# 隐藏箭头
t.hideturtle()




