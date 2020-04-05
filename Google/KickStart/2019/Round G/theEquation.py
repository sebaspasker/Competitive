# the laws of the universe --> N non-negative integers. 
# 	- Ai the i-th of these integers
# 	- Universe --> good if non-negative integer k such that (A1 xor k) + (A2 xor k) + ...(AN xor k) <= M
# 	- k?

# Input
# 	- First T 
# 	- N, M = the number of integers in A and the limit of the equation
# 	- N integers --> The i-th of which is Ai

def xorFunction(A, value, N):
 	kTotal = 0
 	k = value
 	for i in range(0, N):
 		kTotal += A[i] ^ k
 	return kTotal

# def simpleAlgorithm(A, M, N):
# 	i = 1
# 	j = M-1
# 	resultK = 0

# 	while(True):
# 		k1 = xorFunction(A, i, N)
# 		k2 = xorFunction(A, j, N)
# 		middle = j/2
# 		if k2 > k1 and k2 < M:
# 			j = middle
# 			resultK = k2
# 		else if k1 >= M or k1/resultK == 1:
# 			break
# 		else:
# 			i = middle
# 			resultK = k1

def simpleAlgorithm(N, M, A):
	maxK = -1
	binM = list(bin(M))
	binM.pop(0)
	binM.pop(0)
	maxM = 1
	for i in range(0, len(binM)-1):
		maxM = maxM*10+1

	for i in range(0, maxM):
		possibleK = xorFunction(A, i, N)
		if possibleK <= M:
			maxK = possibleK
		else:
			break
		return maxK


T = int(input())
A = []
for x in range(0,T):
	N, M = map(int, input().split())
	A = list(map(int, input().split()))
	max = simpleAlgorithm(N,M,A)
	printf("Case #{}: {}".format(x+1, max))




