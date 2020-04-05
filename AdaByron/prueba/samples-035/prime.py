def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True    

L = []
prime = 0
while True:
    try:
        L.append(int(input()))
    except:
        break
for l in L:
    if is_prime(l):
        prime = prime+1
if prime>1:
    print("{} prime numbers were found!".format(prime))
elif prime==1:
    print("Only one prime number was found!")
else:
    print("No prime number were found!")
