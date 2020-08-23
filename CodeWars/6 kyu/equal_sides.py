def find_even_index(arr):
    suml = 0
    for i in range(0, len(arr)):
        L = arr[:i]
        L2 = arr[i+1:]
        if sum(L) == sum(L2):
            return i
    return -1
