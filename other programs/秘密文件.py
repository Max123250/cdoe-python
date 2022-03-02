import pickle
word = input("输入你要保存的文字：")
fl_name = input("输入文件名：")
ud_name = input("输入文件的后缀名：")
file = open(fl_name+"."+ud_name,"w")
pickle.dump(word,file)
file.close()

