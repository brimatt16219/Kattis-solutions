s = input()

e = 0
for i in range(len(s)):
  if s[i:i + 1] == 'e':
    e += 1

e *= 2

x = ""
for i in range(e):
  x += "e"

print(s[0:1] + x + s[len(s) - 1:len(s)])

  
