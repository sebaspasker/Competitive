T = int(input())
for x in range(0, T):
    N, D = map(int, input().split())
    L = list(map(int, input().split()))
    num = D
    for i in reversed(L):
            div = num//i
            last = div*i
            num = last
    print("Case #{}: {}".format(x+1, num))
