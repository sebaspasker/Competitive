def get_sum(a,b):
    if a > b:
        x = a
        a = b
        b = x
    res = a
    while a != b:
        a += 1
        res += a
    return res
