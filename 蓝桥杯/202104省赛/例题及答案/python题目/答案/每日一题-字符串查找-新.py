key = input()
se = input()

key_list = []
r = 0
index = 0
key = key.upper()
se = se.upper()
first_index = -1
word_len = len(key)
list_len = 0

while r >= 0:
    r = se.find(key,index)
    index = r + len(key)

    if r != -1:

        if r == 0:
            if se[r + word_len] == " ":
                key_list.append(r)

        elif r == len(se) - 1:
            if se[r - word_len] == " ":
                key_list.append(r)

        else:
            if se[r + word_len] == " " and se[r - word_len] == " ":
                key_list.append(r)

    else:
        break
list_len = len(key_list)
if list_len == 0:
    list_len = -1
    print(list_len)
else:
    print(list_len)
    print(key_list[0])
