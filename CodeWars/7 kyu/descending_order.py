def descending_order(num):
    L = [int(x) for x in str(num)]
    L.sort()
    L.reverse()
    return int("".join(str(x) for x in L))
