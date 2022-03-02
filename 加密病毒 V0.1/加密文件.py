import os
path = os.getcwd()
dir_l = os.listdir(path)
text_l = []
for text in dir_l:
    if "." in text:
        text_l.append(text)
for name in text_l:
    file = open(name,"r+",encoding="UTF-8")
    lines = file.readline()
    for line in lines:
        line.strip("\n")
        file.write("".join(lines))
print(lines)
file.close()