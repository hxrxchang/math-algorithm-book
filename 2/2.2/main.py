# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_e
N = int(input())
A = map(int, input().split())

sum = 0
for a in A:
  sum += a

print(sum % 100)


