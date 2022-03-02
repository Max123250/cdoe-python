c = 0 # 统计个数
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            s = 31*10000+i*1000+j*100+k*10+k
            if s%16==0 and s%46==0:
                print(s)
                c += 1
print(c)





        
