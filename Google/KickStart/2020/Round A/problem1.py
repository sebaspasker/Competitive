T = int(input())
for x in range(0, T):
    N, B = map(int, input().split()) 
    L = list(map(int, input().split()))
    L.sort()
    cases = 0
    for l in L:
        if(B >= l):
            cases += 1
            B -= l
        else:
            break
    print("Case #{}: {}".format(x+1, cases))
