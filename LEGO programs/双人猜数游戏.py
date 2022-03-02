import random
def csyx():
    sjs=random.randint(0,100)
    cds=-1
    p1_time=0
    p2_time=0
    ying=0
    while sjs!=cds:
        cds=int(input("player1 enter the guess:"))
        if sjs>cds:
            print("small")
            p1_time=p1_time+1
        elif sjs<cds:
            print("big")
            p1_time=p1_time+1
        else:
            ying=1
            break
        cds=int(input("player2 enter the guess:"))
        if sjs>cds:
            print("small")
            p2_time=p2_time+1
        elif sjs<cds:
            print("big")
            p2_time=p2_time+1
            ying=2
    print("player1 have ",p1_time," time")
    print("player2 have ",p2_time," time")
    if ying==1:
        print("player1 win!")
    else:
        print("player2 win!")
while True:
    over_or_play=int(input("if you want to play,please enter 1.or if you want to exit,please enter 2."))
    if over_or_play==1:
        csyx()
    else:
        break
