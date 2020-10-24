T = int(input())
for x in range(0, T):
    str = input()
    begin = 0
    tot_k = 0
    tot = 0
    while True:
        f_s = str.find("START", begin, len(str))
        if f_s == -1:
            break
        else:
            while True:
                f_k = str.find("KICK", begin, f_s)
                if f_k == -1 or f_k > f_s:
                    break
                else:
                    tot_k += 1
                    begin = f_k + 1
            tot += tot_k
            begin = f_s + 1
    print("Case #{}: {}".format(x+1, tot))
