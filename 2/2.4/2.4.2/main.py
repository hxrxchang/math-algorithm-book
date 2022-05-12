N = int(input())
X = int(input())
Y = int(input())

count = 0
for i in range(0, N):
  if i % X == 0 or i % Y == 0:
    count += 1

print(count)

