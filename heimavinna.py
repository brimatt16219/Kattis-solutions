n = input()

a = n.split(";")

total = len(a)


for i in range(len(a)):
  if (a[i].find("-") != -1):
    b = a[i].split("-")
    c = int(b[1]) - int(b[0])
    total += c

print(total)