import random,time
def yx():
    sjs=random.randint(1,100)
    aisr=["大","小"]
    answer=0
    yhsr=int(input("随机数已出好。请输入您猜的大小："))
    yhdz=(input("请输入您的赌注：")
    aisr=random.choice(aisr)
    aidz=random.randint(1,400)
    print("AI已猜好并下好赌注。")
    print("AI猜的大小为：",aisr)
    print("AI下的赌注为：",aidz)
    print("公布答案！随机数为：",sjs)
    if sjs>50:
        answer="大"
    else:
        answer="小"

coin=0
print("您好，欢迎游玩本游戏。本游戏需要填写用户信息才能游玩。")
name=input("请输入用户名：")
age=int(input("请输入年龄："))
if age>18:
    coin=500
    print("欢迎您！您的初始金币为：",coin)
elif age<18 and age>10:
    coin=400
    print("根据未成年实名认证规则，您的初始金币为：",coin)
else:
    coin=200
    print("根据未成年实名认证规则，您的初始金币为：",coin)
go=True
while go
    cz=input("您可以选择：A.查看金币   B.开始游玩   C.退出游戏   D.查看规则。请输入：")
    if "A" or "a" in cz:
        print("您的金币有：",coin)
    elif "B" or "b" in cz:
        print("开始游戏。")
        yx()
    elif "C" or "c" in cz:
        go=False
    else:
        print("本游戏基本规则为猜数字大小，0到50为小，51到100为大。")
        time.sleep(1)
        print("在猜完大小后，您需要根据您的判断下赌注。")
        time.sleep(1)
        print("游戏开始前系统会根据您的年龄发放金币。")
        time.sleep(1)
        print("祝您游戏愉快。")



