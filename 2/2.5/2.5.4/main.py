N = int(input())

def isPrime(x):
  for i in range(2, x):
   if x % i == 0:
    return False
  return True

results = []
for i in range(2, N + 1):
  if isPrime(i):
    results.append(i)

print(*results)
