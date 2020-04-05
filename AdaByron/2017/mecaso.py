
while True:
    N = int(input()) 
    if N == 0:
        exit(0)
    lNum = list(map(int, input().split()))
    total = 0
    for num in lNum:
        total = total + num 
    print(total)
