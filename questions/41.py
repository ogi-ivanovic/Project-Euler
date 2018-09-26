from itertools import permutations
from math import *

def prime(x):
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

x = 0
pans = []
for i in range(1, 10):
  x = str((x * 10) + i)
  perms = perm(x)
  x = int(x)
  for j in perms:
    pans.append(j)
  
for i in range(-1, -1000000000, -1):
  if prime(pans[i]):
    print(pans[i])
    break

def pandigital(num, digits):
  x = [0]*digits
  while num > 0:
    y = int(num % 10)
    x[y - 1] += 1
    num = int((num - y)/10)
  for i in x:
    if i != 1:
      return False
  return True
