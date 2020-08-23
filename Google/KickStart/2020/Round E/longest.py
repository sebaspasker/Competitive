T = int(input())
for x in range(0, T):
    N = int(input())
    L = list(map(int, input().split()))
    maxres = 0
    res = 0
    ant = -1
    antdiff = -1
    diff = -1
    first = True
    r = []
    for n in L:
        if first:
            first = False
        else:
            # print(ant, n)
            diff = ant-n
            if antdiff == diff:
                r.append(n)
            else:
                r.clear()
                r.append(ant)
                r.append(n)
            maxres = max(len(r), maxres)
        antdiff = diff
        ant = n
    print("Case #{}: {}".format(x+1, maxres))
