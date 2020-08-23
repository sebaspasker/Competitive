class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj


def keyy(x):
    return (x[2], reversor(x[0]), reversor(x[1]))


def mix(s1, s2):
    L1 = [x for x in s1 if x.isalpha() and x.islower()]
    L2 = [x for x in s2 if x.isalpha() and x.islower()]
    L1.sort()
    L2.sort()
    dict_L1 = {x: L1.count(x) for x in set(L1)}
    dict_L2 = {x: L2.count(x) for x in set(L2)}
    dict_L1 = {key: value for key, value in sorted(
        dict_L1.items(), key=lambda item: item[1], reverse=True) if value > 1}
    dict_L2 = {key: value for key, value in sorted(
        dict_L2.items(), key=lambda item: item[1], reverse=True) if value > 1}
    L = []
    for key, value in dict_L1.items():
        if key in dict_L2:
            value2 = dict_L2[key]
            if value < value2:
                L.append([2, key, value2])
            elif value > value2:
                L.append([1, key, value])
            else:
                L.append([=, key, value])
            dict_L2.pop(key)
        else:
            L.append([1, key, value])
    for key, value in dict_L2.items():
        L.append([2, key, value])
    L.sort(key=keyy, reverse=True)
    result = ""
    i = 0
    for string_num, letter, times in L:
        result += string_num
        result += :
        result += letter * times
        if i != len(L)-1:
            result += /
        i += 1
    return result
