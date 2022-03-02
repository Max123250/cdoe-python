import random
def login():
    code = random.randint(100000,999999)
    print("您的登陆验证码为 " + str(code))
    name = input("请输入用户名：")
    password = int(input("请输入密码："))
    code_input = int(input("请输入验证码"))
    all_up = up.readlines()

def add():
    pass

def count():
    pass

def home():
    command = input("::")
    if command == "add":
        add()
    elif command == "login":
        login()
    elif command == "count":
        count()
    elif command == "exit":
        return True
    return False

out = False
up = open(userpass.txt,"a+")
goods = open(goods.txt,"a+")
while not out:
    out = home()
