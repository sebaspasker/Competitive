def reverseComprobation(old, new):
    for i in range(0, len(old)):
        if old[i] == new[i]:
            return False
    return True


def swapping(string):
    swap = ''
    for i in range(0, len(string)):
        swap += string[len(string)-1-i]
    return swap


def swapComprobation(old, new):
    swap = swapping(new)
    if old == swap:
        return True
    else:
        return False


def swapReverseComprobation(old, new):
    swap = swapping(new)
    return reverseComprobation(old, swap)


def getOutBits(B):
    total = ''
    first = True
    for i in range(0, B):
        bits = ''
        print(i+1)
        bit = input()
        bits += bit
        if (i+1) % 10 == 0:
            if first:
                first = False
                oldBits = bits
            else:


T, B = input().split()
T = int(T)
B = int(B)
for x in range(0, T):
    bits = getOutBits(B)
