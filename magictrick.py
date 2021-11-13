
n = input("")
guess = True

for char in n:
  if n.count(char) > 1:
    guess = False

if guess:
  print(1)
else:
  print(0)