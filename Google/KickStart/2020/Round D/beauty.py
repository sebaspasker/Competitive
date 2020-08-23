# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd
# NO CONSEGUIDO
# Para 3 nodos en ese nivel 9 casos
# 1 2 3
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

# Calculo 1 de cada nivel -> resultado
# Multiplico por (numero de nodo en el nivel ^ 2)

class Node():
    Parent = None
    num = 0
    sons = []


def Level(node):
    return LevelIt(node, 0)


def LevelMaxHoja(root):
    return LevelMaxHojaIt(root, 1)


def LevelMaxHojaIt(node, num):
    num2 = num + 1
    if len(node.sons) == 0:
        return num
    else:
        m = 0
        for son in node.sons:
            m = max(m, LevelMaxHojaIt(son, num2))
        return m


def LevelIt(node, num):
    num += 1
    if node.Parent is None:
        return num
    else:
        return LevelIt(node.Parent, num)


def numNodesLevel(root, num):
    return numNodesLevelIt(root, num)


def numNodesLevelIt(node, num):
    num2 = num - 1
    if num2 == 0:
        return 1
    else:
        n = 0
        for son in node.sons:
            n += numNodesLevelIt(son, num2)
        return n


def baseCaseIt(n, level, it):
    it2 = it + 1
    level2 = level - n
    if level2 < 1:
        return it2
    else:
        return baseCaseIt(n, level2, it2)


def baseCase(a, level):
    return baseCaseIt(a, level, 0)


T = int(input())
for x in range(0, T):
    n, a, b = map(int, input().split())
    L = list(map(int, input().split()))
    nodeList = []
    root = Node()
    root.num = 1
    nodeList.append(root)
    avg = 0.0
    tot = 0.0
    # Creo arbol
    for i in range(0, n-1):
        node = Node()
        node.num = i + 2
        node.Parent = nodeList[L[i]-1]
        node.sons = []
        nodeList[L[i]-1].sons.append(node)
        nodeList.append(node)
    lresultsa = []
    lresultsb = []
    nodos = []
    for i in range(1, LevelMaxHoja(root)+1):
        result1 = baseCase(a, i)
        result2 = baseCase(b, i)
        nodos.append(numNodesLevel(root, i))
        lresultsa.append(result1)
        lresultsb.append(result2)
    for i in range(0, len(lresultsa)):
        numNodosa = nodos[i]
        resultadoa = lresultsa[i]
        for j in range(0, len(lresultsa)):
            if i != j:
                numNodosb = nodos[j]
                resultadob = lresultsb[j]
                avg += numNodosa*resultadoa + numNodosb*resultadob
                # tot += numNodosa + numNodosb
                tot += resultadoa + resultadob
    print(avg/tot)
    print(lresultsa)
    print(lresultsb)
    print(nodos)
    break
