"""Stable Wall Google Kickstart Round C 2020"""

T = int(input())
for x in range(0, T):
    R, C = map(int, input().split())
    L = []
    Lsol = []
    variables = []
    options = []
    result = ''
    w = ' '
    for i in range(0, R):
        L.append(list(input()))
        Lsol.append([w for j in range(0, C)])
    for i in reversed(range(1, R)):
        colOptions = []
        for j in range(0, C):
            if not variables.contains(L[i][j]):
                variables.append(L[i][j])
            if not options.contains(L[i][j]) and options.contains(L[i-1][j]):
                result = '-1'
                break
        if result == '-1':
            break
            # If No está en la lista de opciones L[i][j] y L[i+1][j] es tampoco
