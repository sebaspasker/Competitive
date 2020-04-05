T = int(input())
for x in range(0, T):
    L = input()
    s = ""
    actualH = 0
    for i in range((len(L))):
        num = int(L[i])
        if actualH < num:
            while actualH < num:
                s += '('
                actualH += 1
            s += str(num)
        elif actualH > num:
            while actualH > num:
                s += ')'
                actualH -= 1
            s += str(num)
        else:
            s += str(num)
    while actualH > 0:
        s += ')'
        actualH -= 1
    print("Case #{}: {}".format(x+1, s))
