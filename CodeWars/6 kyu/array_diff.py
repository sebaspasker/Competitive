import numpy

def array_diff(a, b):
    return [x for x in a if x not in set(b)]
