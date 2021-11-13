a, b = map(int, input().split())

c = abs(b - a) + 1
d = 0
if a > b:
  d = b
else:
  d = a

for i in range(c):
  print(d + i + 1)