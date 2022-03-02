for i in range(1,9+1):
    for j in range(1,9+1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end = " ")
        if i == j:
            break
    print()
