def duplicate_count(text):
    # Your code goes here
    text = text.lower()
    vars = list(set(text))
    tot = 0
    for var in vars:
        if text.count(var) > 1:
            tot += 1
    return tot
