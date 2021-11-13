n = int(input())

a = []

for i in range(n):
  a.append(input())

s = len(a) + (len(a) % 2 - 1)

for i in range(0, s, 2):
  print(a[i])