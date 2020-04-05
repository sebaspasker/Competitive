T = int(input())
for x in range(0, T):
    N, K, P = map(int, input().split())
    Llist = []
    for i in range(0, N):
        L = list(map(int, input().split()))
        Llist.append(L)
    if K <= P:
        r = K
    else:
        r = P
    XList = []
    for i in range(0, N):
        List = []
        for j in range(0, r):
            List.append(0)
        XList.append(List)
    for i in range(0, N):
        anterior = 0
        for j in range(0, r):
            benefit = Llist[i][j]
            XList[i][j] = anterior + benefit
            anterior = anterior + benefit
    using = 0
    anterior = 0
    max = 0
    maxr = 0
    for i in range(0, N):
        for j in range(0,r):
            if using < P:
                max -= anterior
                max += Xlist[i][j]
                using +=1
                anterior = Llist[i][j]
            else:
               if max - anterior + Llist[i][j] > max:
                   max -= anterior
                   max += Llist[i][j]
                   anterior = Llist[i][j]
