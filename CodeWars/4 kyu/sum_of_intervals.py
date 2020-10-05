def sum_of_intervals(intervals):
    L_set = list(set(intervals))
    L_set.sort(key=lambda x: x[0])
    first = True
    sum = 0
    for interval in L_set:
        if first:
            i_min = interval[0]
            i_max = interval[1]
            sum += i_max - i_min
            first = False
        elif interval[0] <= i_max:
            i_min = i_max
            i_max = max(i_max, interval[1])
            sum += i_max - i_min
        else:
            i_min = interval[0]
            i_max = interval[1]
            sum += i_max - i_min
    return sum
