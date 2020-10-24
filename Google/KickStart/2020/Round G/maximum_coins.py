T = int(input())
for x in range(0, T):
    N = int(input())
    M = []
    for i in range(N):
        N = list(map(int, input().split()))
        M.append(N)
    lim_C = len(M)-1
    lim_F = 0
    for i in reversed(range(0, len(M))):
        F = 0
        C = i
        while True:
            print(C, F)
            if C > lim_C or F > lim_F:
                break
            C += 1
            F += 1
        lim_F += 1
        lim_C -= 1
