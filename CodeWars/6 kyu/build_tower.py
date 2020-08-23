def tower_builder(n_floors):
    res = []
    tot = n_floors*2 - 1
    for n in reversed(range(0, n_floors)):
        str = list("*" * tot)
        for i, j in zip(range(0, n), range(tot-n, tot)):
            str[i] = " "
            str[j] = " "
        res.append("".join(x for x in str))
    return res
