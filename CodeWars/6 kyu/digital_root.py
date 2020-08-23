def digital_root(n):
    L = list(map(int, str(n)))
    res = 0
    for ln in L:
        res += ln
    if len(str(res)) > 1:
        return digital_root(res)
    else:
        return res
