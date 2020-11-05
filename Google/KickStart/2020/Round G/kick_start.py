# 2 Test TLE

T = int(input())
for x in range(0, T):
    str = input()
    begin = 0
    num_k = []
    num_s = []
    while True:
        f_k = str.find("KICK", begin, len(str))
        if f_k == -1:
            break
        else:
            num_k.append(f_k)
            begin = f_k + 1
    begin = 0
    while True:
        f_s = str.find("START", begin, len(str))
        if f_s == -1:
            break
        else:
            num_s.append(f_s)
            begin = f_s + 1
    print("Case #{}: {}".format(x+1, x))
