T = int(input())
for x in range(T):
    N, K = map(int, input().split())
    L = []
    for i in range(N):
        S, E = map(int, input().split())
        L.append([S, E])
    L.sort()
    last = -1
    ans = 0
    for interval in L:
        last = max(last, interval[0])
        needs = interval[1] - last
        if needs > 0:
            needs = (needs - 1) // K + 1
            ans += needs
            last += needs * K
    print("Case #{}: {}".format(x + 1, ans))
print("Hola que tal")
