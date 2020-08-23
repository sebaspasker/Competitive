"""
Office campus
1 to n office buildings in line
1 to n height meters

To Andre, a building x is visible if and only if there is no building
to the left of building x that is strictly higher than building x.
Similarly, to Sule, a building x is visible if and only if there is
no building to the right of building x that is strictly higher than building x.

A visible to Andre
B visible to Sule
C visible to both

They give you N, A, B and C -> possible height construction
"""

T = int(input())
for x in range(0, T):
    print("Case #{}:".format(x+1), end=" ")
    N, A, B, C = map(int, input().split())
    if A + B - C > N or (A+B-C == 1 and N >= 2):
        print("IMPOSSIBLE")
    else:
        if N == 1:
            print("1")
        elif N == 2:
            if C == 2:
                print("1 1")
            elif A == 2:
                print("1 2")
            elif B == 2:
                print("2 1")
        else:
            res = []
            for i in range(0, A-C):
                res.append(2)
            for i in range(0, C):
                res.append(3)
            for i in range(0, B-C):
                res.append(2)
            extra = N - (A + B - C)
            for i in range(0, extra):
                res.insert(i, 1)
            for r in res:
                print("{}".format(r), end=" ")
            print()
