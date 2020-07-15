"""
possible_note = 0 <= x <= 3
(OR)
si possible_note_1 > 3
	count++
	renicio
si possible_note_2 < 0
	count++
	possible_note_2 = 3
	renicio
"""

# 0 y 3
# 1 y 4  
# 2 y 5
# 3 y 6
# --- 4 y 7 --
# Renicio 
# count ++
# 0 y 3

# 0 y 3
# 1 y 4  
# 2 y 5
# 3 y 6
# 2 y 5
# 1 y 4
# 0 y 3
# -1 y 2
# Renicio 
# count ++
# 0 y 3

T = int(input())
for x in range(0, T):
    n = int(input())
    L = list(map(int, input().split()))
    possible_note_1 = 0
    possible_note_2 = 3
    prev = L[0]
    count = 0
    for i in range(1, n):
        if prev > L[i]:
            possible_note_2 -= 1
            # Dice que puede bajar a cualquier nota, por lo que nos ponemos
            # en el mejor de los casos solo en el caso de reduccion
            possible_note_1 = 0
        if prev < L[i]:
            possible_note_1 += 1
            possible_note_2 = 3
        prev = L[i]
        if possible_note_1 > 3 or possible_note_2 < 0:
            count += 1
            possible_note_1 = 0
            possible_note_2 = 3
    print("Case #{}: {}".format(x+1, count))
            
