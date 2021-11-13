
a = 1
b = 0
c = 0
#100

abc = input()

for i in range(len(abc)):
  let = abc[i: i + 1]
  if let == 'A':
    a,b = b, a
  if let == 'B':
    b,c = c, b
  if let == 'C':
    a,c = c, a

if (a == 1):
  print("1")
if (b == 1):
  print("2")
if (c == 1):
  print("3")


        

  
