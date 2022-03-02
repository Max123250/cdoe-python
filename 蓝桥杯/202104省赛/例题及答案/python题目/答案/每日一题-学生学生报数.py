num = int(input())
st = list(range(1,num+1))
kick_num = 2
while True:
    st.pop(kick_num)
    kick_num = (kick_num + 2) % len(st)
    if len(st) == 1:
        break
print(st[0])
