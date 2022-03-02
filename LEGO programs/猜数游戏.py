import random
while True:
    sjs=random.randint(0,100)
    cds=-1
    while sjs!=cds:
        cds=int(input("enter your guess:"))
        if sjs>cds:
            print("small")
        elif sjs<cds:
            print("big")
    print("bingo!")
    
    
