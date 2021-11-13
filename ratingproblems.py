n, k = map(int, input().split())

l = 0
w = 0
for i in range(k):
  p = int(input())
  l += p
  w += p

r = n - k
l += r * -3
w += r * 3

l /= n
w /= n

print(str(l) + " " + str(w))