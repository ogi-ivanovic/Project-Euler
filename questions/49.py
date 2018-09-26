from math import *

def prime(x):
  if x <= 1:
    return False
  if (x % 2 == 0) and (x != 2):
    return False
  for i in range(3, int(sqrt(x)) + 1, 2):
    if x % i == 0:
      return False
  return True

def permsOfEachOther(x, y):
  z1 = [0]*10
  z2 = [0]*10
  for i in range(4):
    a = int(x % 10)
    b = int(y % 10)
    z1[a] += 1
    z2[b] += 1
    x = int((x - a)/10)
    y = int((y - b)/10)
  return z1 == z2

def pat(x):
  a = x
  b = x + 3330
  c = b + 3330
  if prime(a) and prime(b) and prime(c):
    if permsOfEachOther(a, b) and permsOfEachOther(b, c):
      if x != 1487:
        return str(a) + str(b) + str(c)
  return 'no'

for i in range(1000, 3400):
  x = pat(i)
  if x != 'no':
    print(x)
    break
