from math import *

def choose(n, r):
  c = int((factorial(n))/(factorial(r) * (factorial(n - r))))
  return c

count = 0
for n in range(1, 101):
  for r in range (1, n + 1):
    c = choose(n, r)
    if c > 1000000:
      count += 1
print(count)
