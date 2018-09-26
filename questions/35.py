from itertools import permutations
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

def perm(x):
  perm = permutations(x)
  perms = []
  for i in list(perm):
    num = ''
    for j in i:
      num = num + j
    num = int(num)
    perms.append(num)
  return perms

def rotations(x, len):
  rots = [int(x)]
  for i in range(len - 1):
    x = x[-1] + x[0:len-1]
    rots.append(int(x))
  return rots

def circular(x):
  rots = rotations(str(x), len(str(x)))
  length = len(rots)
  for i in range(1, length):
    if not prime(rots[i]):
      return False
  return True

count = 0
for i in range(1, 1000000):
  if prime(i):
    if circular(i):
      count += 1
print(count)
