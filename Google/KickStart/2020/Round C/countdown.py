"""Countdown Google Kickstart problem 2020 Round C."""
T = int(input())


for x in range(0, T):
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    tot = 0
    for i in range(0, N):
        if L[i] == K:
            uncount = K-1
            for j in range(i+1, N):
                if uncount != L[j]:
                    break
                elif uncount == L[j] == 1:
                    tot += 1
                    break
                elif uncount == L[j]:
                    uncount -= 1
    print("Case #{}: {}".format(x+1, tot))
