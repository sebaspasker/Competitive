def keyy(elem):
    return elem[0]


T = int(input())
for x in range(0, T):
    N = int(input())
    L = []
    for i in range(0, N):
        h, e = map(int, input().split())
        L.append([h, e, ""])
    L2 = []
    for l in L:
        L2.append(l)
    L2.sort(key=keyy)
    cEnd = -1
    jEnd = -1
    s = ""
    for l in L2:
        begin = l[0]
        end = l[1]
        if cEnd <= begin:
            l[2] = "C"
            cEnd = end
        elif jEnd <= begin:
            l[2] = "J"
            jEnd = end
        else:
            s = "IMPOSSIBLE"
            break
    if s != "IMPOSSIBLE":
        s = ""
        for l in L:
            s += l[2]
    print("Case #{}: {}".format(x+1, s))
