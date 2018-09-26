from math import *

def solutions(p):
  solutions = 0
  for a in range(1, 1000):
    for b in range(a, 1000):
      c = sqrt(a**2 + b**2)
      if a + b + c > p:
        break
      if c - int(c) != 0:
        continue
      if a + b + c == p:
        solutions += 1
  return solutions
      
max = 0
maxi = 0

for i in range(1, 1001):
  print(i)
  x = solutions(i)
  if x > max:
    maxi = i
    max = x
print(maxi)
