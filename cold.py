
n = int(input())

a = [int(x) for x in input().split()]
d = 0
for i in a:
  if i < 0:
    d += 1
print(d)