import easygui as e
import sys
def login():
    global us,ua,login_num
    ui = e.multpasswordbox("Enter your information to login.", "Login", (["User name", "Password"]))
    if not ui[0] in us:
        ln_or_rger = e.buttonbox("Wrong user name！Please register or login again!","error",["login","register"])
        if ln_or_rger == "login":
            login()
        else:
            register()
    else:
        where = us.index(ui[0])
        if not ui[1] == ua[where]:
            l_or_r = e.buttonbox("Wrong password!login again!", "error", ["login"])
            if l_or_r == "login":
                login()
        else:
            e.msgbox("Welcome！", "Logged in")
            login_num = 1
def register():
    global us,ua
    ui = e.multpasswordbox("Enter your information to register.", "Register", (["User name", "password"]))
    us.append(ui[0])
    ua.append(ui[1])
def answer(lt,an):
        if an in lt:
            return 20
        else:
            return 0
def question():
    f1=0
    an1=e.buttonbox(msg="我是谁？",title="猜猜我是谁？"
                    ,image="龙骨炮.jpg"
                    ,choices=["A.龙骨炮","B.龙头","C.贾撕特重鸡脖"])
    an2=e.buttonbox(msg="我是谁？",title="猜猜我是谁？"
                    ,image="sans.jpg"
                    ,choices=["A.Sans","B.Alphys","C.Toby"])
    an3=e.buttonbox(msg="我是谁？",title="猜猜我是谁？"
                    ,image="papyrus.jpg"
                    ,choices=["A.Totiel","B.Flowey","C.Papyrus"])
    an4=e.buttonbox(msg="我是谁？",title="猜猜我是谁？"
                    ,image="flowey.jpg"
                    ,choices=["A.Flowey","B.Undyue","C.Mettaton"])
    an5=e.buttonbox(msg="我是谁？",title="猜猜我是谁？"
                    ,image="asriel.jpg"
                    ,choices=["A.Totriel","B.Frisk","C.Asriel"])

    f1+=answer(an1,"A")
    f1+=answer(an2,"A")
    f1+=answer(an3,"C")
    f1+=answer(an4,"A")
    f1+=answer(an5,"C")
    f=str(f1)
    q="you have "+f+" fraction"
    if f1==100:
        e.msgbox(msg=q,title="最终分数",image="100.jpg")
    elif f1==80:
        e.msgbox(msg=q,title="最终分数",image="80.jpg")
    elif f1==60:
        e.msgbox(msg=q,title="最终分数",image="60.jpg")
    elif f1==40:
        e.msgbox(msg=q,title="最终分数",image="40.jpg")
    elif f1==20:
        e.msgbox(msg=q,title="最终分数",image="20.jpg")
    else:
        e.msgbox(msg=q,title="最终分数",image="0.jpg")
us = ["Max"]
ua = ["123"]
login_num = 0
while True:
    if login_num == 0:    
        choice = e.buttonbox("Welcome!\nyou haven't loaned.", "Menu", ["login", "register", "question"])
    else:
        choice = e.buttonbox("Welcome!\nyou have loaned.", "Menu", ["login", "register", "question"])
    if choice == "login":
        login()
    elif choice == "register":
        register()
        e.msgbox("Login again after register.", "Tips")
        login()
    elif choice == "question":
        if login_num == 1:
            question()
        else:
            l_or_r = e.buttonbox("you didn't login!Please register or log in first.","Tips",["login","register"])
            if l_or_r == "login":
                login()
            else:
                register()
    else:
        sys.exit()