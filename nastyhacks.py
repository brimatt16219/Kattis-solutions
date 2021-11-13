
n = int(input())

a = [""]

for i in range(n):
  r, e, c = map(int, input().split())
  if e - c > r:
    a.append("advertise")
  elif e - c == r:
    a.append("does not matter")
  elif e - c < r:
    a.append("do not advertise")

for i in a:
  print(i)
