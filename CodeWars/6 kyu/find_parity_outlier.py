def find_outlier(integers):
    first_three = integers[0:3]
    even = sum(1 for i in first_three if i % 2 == 0)
    if even > 1:
        for i in integers:
            if i % 2 == 1:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i
