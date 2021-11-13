
n = int(input())

total = 0

for i in range(n):
  n1, n2 = map(float, input().split())
  total += n1 * n2

print(total)
