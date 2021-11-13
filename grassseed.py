s = float(input())

l = int(input())

c = 0
for i in range(l):
  a, b = map(float, input().split())
  c += a * b

c *= s
print(c)