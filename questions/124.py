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

nums = [0]*100000
nums[0] = 1
nums[1] = 1
for i in range(2, 100000):
  if nums[i] == 0 and prime(i):
    for j in range(i*2, 100000, i):
      nums[j] = 1
primes = [2]
for i in range(3, 100000, 2):
  if nums[i] == 0:
    primes.append(i)


def radCore(num, lastDiv, divProd):
  if num == 1:
    return divProd
  for i in range(lastDiv + 1, num + 1):
    if num % i == 0 and i in primes:
      lastDiv = i
      while num % lastDiv == 0:
        num = int(num / lastDiv)
      divProd *= lastDiv
      break
  return radCore(num, lastDiv, divProd)

def rad(num):
  return radCore(num, 1, 1)

rads = []
for n in range(1, 100001):
  print(n)
  rads.append([rad(n), n])

rads.sort()

print(rads[9999])
