t = int(input())
b = []

for i in range(t):
  n = int(input())
  a = []

  for j in range(n):
    a.append(input())

  leng = len(a)
  i = 0
  while i < leng:
    j = i + 1
    while j < leng:
      if (a[i] == a[j]):
        a.remove(a[i])
        j -= 1
        leng -= 1
      j += 1
    i += 1
  b.append(len(a))


for i in b:
  print(i)

        

  
