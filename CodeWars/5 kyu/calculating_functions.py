def zero(entry=None): #your code here
    if entry is None:
        return 0
    else:
        return entry(0)
    
def one(entry=None): #your code here
    if entry is None:
        return 1
    else:
        return entry(1)
    
def two(entry=None): #your code here
    if entry is None:
        return 2
    else:
        return entry(2)
    
def three(entry=None): #your code here
    if entry is None:
        return 3
    else:
        return entry(3)
    
def four(entry=None): #your code here
    if entry is None:
        return 4
    else:
        return entry(4)
    
def five(entry=None): #your code here
    if entry is None:
        return 5
    else:
        return entry(5)
def six(entry=None): #your code here
    if entry is None:
        return 6
    else:
        return entry(6)
    
def seven(entry=None): #your code here
    if entry is None:
        return 7
    else:
        return entry(7)
    
def eight(entry=None): #your code here
    if entry is None:
        return 8
    else:
        return entry(8)
    
def nine(entry=None): #your code here
    if entry is None:
        return 9
    else:
        return entry(9)

def plus(num): #your code here
    return lambda x: x + num
def minus(num): #your code here
    return lambda x: x - num
def times(num): #your code here
    return lambda x: x * num
def divided_by(num): #your code here
    return lambda x: x // num
