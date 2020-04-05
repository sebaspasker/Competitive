T = int(input())
for x in range(0, T):
    N = int(input())
    L = []
    for i in range(0, N):
        Li = []
        Li = list(map(int, input().split()))
        L.append(Li)
    trace = 0
    for i in range(0, N):
        trace = trace + L[i][i]
    Lt = []
    for i in range(0, N):
        Li = []
        for j in range(0, N):
            Li.append(0)
        Lt.append(Li)
    for i in range(0, N):
        for j in range(0, N):
            Lt[j][i] = L[i][j]
    s = 0
    for l in L:
        l.sort()
        for i in range(0, N-1):
           if(l[i] == l[i+1]):
                s = s+1
                break
    r = 0
    for l in Lt:
        l.sort()
        for i in range(0, N-1):
           if(l[i] == l[i+1]):
                r = r+1
                break
    print("Case #{}: {} {} {}".format(x+1, trace, s, r))
