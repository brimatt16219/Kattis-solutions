
n = int(input())

a = [int(n) for n in input().split()]

total = 0
for i in a:
  if i == -1:
    n -= 1
  else:
    total += i

print(total / n)