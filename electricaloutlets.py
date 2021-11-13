n = int(input())

total = []
for i in range(n):
  a = [int(item) for item in input().split()]
  
  temp = 0
  for j in range(a[0]):
    temp +=a[j + 1]
  
  temp -= (a[0] - 1)
  total.append(temp)
  a = []
for i in total:
  print(i)

