import time
c_time=int(input("countdown timer:How many seconds?"))
for i in range(c_time,0,-1):
    print(i)
    time.sleep(1)
print("Blast off!")