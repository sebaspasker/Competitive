# Es una guarrada pero no me he comido mucho la cabeza
def duplicate_encode(word):
    L = list(word.lower())
    result = ''
    for i in range(0, len(L)):
        char = L[i]
        L2 = L.copy()
        L2.pop(i)
        if char in L2:
            result += ')'
        else:
            result += '('
    return result
