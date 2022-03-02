a = input()
b = input()
c = input()
abc = a + b + c
# 全转成大写字母，
# 不区分大小写往往先都转换成大写
abc = abc.upper() 

letters = []
counts=[]

# set() 函数创建一个无序不重复元素集，
#可进行关系测试，删除重复数据，
#还可以计算交集、差集、并集等。
# print(set(abc))
# 排序
# print(sorted(set(abc)))

for letter in sorted(set(abc)): 
    if letter.isalpha():# 判断是否为字母
        letters.append((letter))
        counts.append(abc.count(letter))
for letter in letters:
    print(letter,end="    ")
print()
for count in counts:
    print(count,end="    ")
