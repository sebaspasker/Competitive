N = int(input())
B = P = 0
while True:
    try:
        B, P = map(int, input().split())
        N = B - P
        if N < 0:
            print("NO")
        else:
            print("SI")
    except (EOFError):
        break

