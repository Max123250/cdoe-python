import RPi.GPIO as GPIO#导入树莓派
GPIO.setwarnings(False)#禁止警报
GPIO.setmode(GPIO.BOARD)

#设置37号引脚为输入状态
GPIO.setup(37,GPIO.IN)
num = 0#记录按钮按下的次数
while num < 10:
    re = GPIO.input(37)
    if re == 0:
        while not re: re = GPIO.input(37)
        num += 1
        print(num)
GPIO.cleanup()#清空程序
