def keyy(x):
    return (x[0], x[1])


T = int(input())
for x in range(T):
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    Lindex = [i + 1 for i in range(0, len(L))]
    Lattemps = []
    for i in L:
        if i/X - i//X == 0.0 and i//X != 0:
            Lattemps.append(i//X - 1)
        else:
            Lattemps.append(i//X)
    Lall = [[attempts, index] for attempts, index in
            zip(Lattemps, Lindex)]
    Lall.sort(key=keyy)
    print("Case #{}: {}".format(x+1, ' '.join([str(i[1]) for i in Lall])))
