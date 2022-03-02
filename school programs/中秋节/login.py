import easygui as gui
file = open("user information.txt","a+")
def login():
    re = gui.multpasswordbox("请输入用户名与密码","调度系统-登录",["用户名","密码"])
    in_file = file.readlines()
    information = []
    l = []
    for x in in_file:
        l.extend(x.strip("\n"))
        if len(l) == 2:
            information.append(l)
            l = []
    for x in information:
        if re == x:
            turn = True


def reg():
    re = gui.multpasswordbox("请输入用户名与密码","调度系统-注册",["用户名","密码"])
    file.write(re[0]+"\n"+re[1]+"\n")

run = True
title = "调度系统-登录"
start = False
while run:
    return_gui = gui.buttonbox("欢迎使用无人观光车调度系统！",title,["登录","注册"])
    if return_gui == "登录":
        login()
    elif return_gui == "注册":
        reg()

file.close()