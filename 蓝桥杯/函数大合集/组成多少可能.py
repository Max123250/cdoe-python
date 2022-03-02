def fun(lst,a,bol):
    #寻找lst内可能组成所有的a位组合，单项内多个元素相同(bol = True,反之则不同）
    #返回列表：[[a,b……]……](a\b均为lst内的某一项
    r = []
    if a == 2:
        for x in lst:
            for y in lst:
                if bol:
                    if x != y:
                        r.append([x,y])
                else:
                    r.append([x,y])
    elif a == 3:
        for x in lst:
            for y in lst:
                for z in lst:
                    if bol:
                        if x != y != z:
                            r.append([x,y,z])
                    else:
                        r.append([x,y,z])
    elif a == 4:
        for x in lst:
            for y in lst:
                for z in lst:
                    for b in lst:
                        if bol:
                            if x != y != z != b:
                                r.append([x,y,z,b])
                        else:
                            r.append([x,y,z,b])
    elif a == 5:
        for x in lst:
            for y in lst:
                for z in lst:
                    for b in lst:
                        for c in lst:
                            if bol:
                                if x != y != z != b != c:
                                    r.append([x,y,z,b,c])
                            else:
                                r.append([x,y,z,b,c])
    return r
'''测试通过'''