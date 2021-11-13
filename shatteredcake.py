l = int(input())

n = int(input())

v = 0

for i in range(n):
  a, b = map(int, input().split())
  v += a * b

print(int(v/l))