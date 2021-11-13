
n = int(input())
total = 0
for i in range(n):
  num = int(input())

  p = num % 10
  base = int(num / 10)

  total += pow(base, p)

print(total)