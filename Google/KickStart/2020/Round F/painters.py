# Min max algorithm
# S = length of piramide
# Alma starts in (Ra, Pa)
# Berthe starts in (Rb, Pb)
# C rooms under construction
# C more lines

class Painter():
    R = -1
    P = -1
    S = -1
    painted_rooms = []
    points = 0
    Finish = False

    def adjacent(self):
        return


def adjacent(painter, available_list):
    R = painter.R
    P = painter.P
    adjacent = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (R+i, P+j) in available_list:
                adjacent.append((R+1, P+j))
    return adjacent


T = int(input())
for x in range(T):
    S, Ra, Pa, Rb, Pb, C = map(int, input().split())
    construction_list = []
    available_list = []
    for i in range(C):
        Ri, Pi = map(int, input().split())
        construction_list.append((Ri, Pi))
    Sj = 1
    for i in range(S):
        for j in range(Sj):
            available_list.append((i+1, j+1))
        Sj += 2
    total_points = 0
    Alma = Painter()
    Alma.R = Ra
    Alma.P = Pa
    Alma.S = S
    Berthe = Painter()
    Berthe.R = Rb
    Berthe.P = Pb
    Berthe.S = S
    print(Berthe.__str__, Berthe.R, Berthe.P)
    print(Alma.__str__, Alma.R, Alma.P)
    print(adjacent(Berthe, available_list))
    print(adjacent(Alma, available_list))
    while True:
        # Alma starts
        # Adjacent comprobation
        break
