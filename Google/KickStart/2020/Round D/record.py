# Isyana is given the number of visitors at her local theme park on N consecutive days. The number of visitors on the i-th day is Vi. A day is record breaking if it satisfies both of the following conditions:
# The number of visitors on the day is strictly larger than the number of visitors on each of the previous days.
# Either it is the last day, or the number of visitors on the day is strictly larger than the number of visitors on the following day.
# Note that the very first day could be a record breaking day!

# Please help Isyana find out the number of record breaking days.

T = int(input())
for x in range(0, T):
    n = int(input())
    L = list(map(int, input().split()))
    max = -1
    count = 0
    for i in range(0, n-1):
        if L[i] > max:
            max = L[i]
            if L[i+1] < max:
                count += 1
    if L[n-1] > max:
        count += 1
    print("Case #{}: {}".format(x+1, count))


