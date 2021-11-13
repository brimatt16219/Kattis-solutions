
plan = int(input())

n = int(input())

leftover = 0

for i in range(n):
  p = int(input())
  leftover += plan - p

print(leftover + plan)

