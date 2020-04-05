T = int(input())
for z in range(0, T):
    n = int(input())
    L = list(map(int, input().split()))
    max = 1
    x = []
    printable = ""
    for i in range(0, n):
        x.append(0)
    for i in range(1, n+1):
        option = L[i-1]
        if(option > n):
            r = n
        else:
            r = option
        for j in range(max, r+1):
            if(option >= j):
                x[j-1] += 1
                if(x[j-1] >= j):
                    max = j
            else:
                break
        printable = printable + " " + str(max)
    print("Case #{}:{}".format(z+1, printable))
