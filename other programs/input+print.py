name=input("your name:")
print("")
print("hello",name,"welcome")
def login():
    print("if you want to use this pro,you must log in.")
    password=input("your password")
    password2=input("your password again")
    if password==password2:
        break
    else:
        print("please try again.")
        login()
print("hello,welcome!")
print("this program was made by max,")
print("continuous updating.")

