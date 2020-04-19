T = int(input())
for i in range(0, T):
    N = int(input())
    L = list(map(int, input().split()))
    lAnterior = -1
    subida = False
    first = True
    x = 0
    for l in L:
        if not first:
            if subida and lAnterior > l:
                subida = False
                x += 1
            elif l > lAnterior:
                subida = True
            else:
                subida = False
        else:
            first = False
        lAnterior = l
    print("Case #{}: {}".format(i+1, x))
