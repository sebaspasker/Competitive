# Lo podria haber hecho con una parámetro de repeticiones y
# asi no tendria que contar cada vez el array, simplemente voy
# acumulando el numero de repeticiones y pasa de n^n a n


def loop(pos, string):
    newpos = pos.copy()
    i = 0
    while True:
        if i == len(string):
            break
        if string[i].isnumeric():
            times = int(string[i])
            parentesis = 0
            for j in range(i+1, len(string)):
                if string[j] == "(":
                    parentesis += 1
                elif string[j] == ")":
                    parentesis -= 1
                if parentesis == 0:
                    for z in range(0, times):
                        newpos = loop(newpos.copy(), string[i+2:j])
                    i = j
                    break
        else:
            if string[i] == "S":
                newpos[1] += 1
            elif string[i] == "N":
                newpos[1] -= 1
            elif string[i] == "E":
                newpos[0] += 1
            elif string[i] == "W":
                newpos[0] -= 1

            if newpos[0] == 0:
                newpos[0] = 10**9
            elif newpos[0] == 10**9+1:
                newpos[0] = 1
            if newpos[1] == 0:
                newpos[1] = 10**9
            elif newpos[1] == 10**9+1:
                newpos[1] = 1
        i += 1
    return newpos


T = int(input())
for x in range(0, T):
    pos = [1, 1]
    string = input()
    newpos = loop(pos, string)
    print("Case #{}: {} {}".format(x+1, newpos[0], newpos[1]))
