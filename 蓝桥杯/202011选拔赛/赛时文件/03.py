#第三题：输入n，输出1到n之间的数的平方
num = int(input())
list = []
for i in range(1,num + 1):
    list.append(str(i*i))
print(",".join(list))
#20分满分