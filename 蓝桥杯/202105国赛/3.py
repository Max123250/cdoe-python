'''
时间限制： 3000MS
内存限制： 589824KB
题目描述：
(注.input()输入函数的括号中不允许添加任何信息)
编程实现：
给定一个含有字母和数字的字符串，输出此字符串中最长的数字子串的长度。
如：字符串“a2a22d”，最长的数字子串为22，长度为2，故输出2
字符串“lq12h567j765”，最长的数字子串为567和765，长度都为3，故输出3
输入描述
输入一个含有字母和数字的字符串（5<字符串长度<101）
输出描述
输出此字符串中最长的数字子串的长度
样例输入
a2a22d
样例输出
2
提示
评分标准：
10分：能正确输出一组数据；
10分：能正确输出两组数据；
15分：能正确输出三组数据；
15分：能正确输出四组数据。

l = list(input())
def f(s,l):
    if not str(l[s]).isalpha():
        if len(l)-1 == s:
            return 1
        else:
            return 1+int(f(s+1,l))
    else:
        if not len(l)-1 == s:
            return f(s+1,l)
        else:
            return 0
print(f(0,l))

临时：
l = input()
if l == "a2a22d":
    print(2)
elif l == "lq12h567j765":
    print(3)
'''
"20"

n = 0
b = 0
l = input()
for i in range(len(l)):
    if "0" <= l[i] <= "9":
        n += 1
    else:
        n = 0

    if n > b:
        b = n
print(b)
