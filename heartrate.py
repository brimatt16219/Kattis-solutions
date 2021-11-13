
n = int(input())

a = []
for i in range(n):
  s = []
  b, p = map(float, input().split())
  integral = 60 / p
  rate = 60 * b / p
  s.append(rate - integral)
  s.append(rate)
  s.append(rate + integral)
  a.append(s)

i = 0
while i < n:

  #print(len(a[0]))
  print(str(round(a[i][0], 4)) + " " + str(round(a[i][1], 4)) + " " + str(round(a[i][2], 4)))
  i += 1


  
