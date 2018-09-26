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

def divsCore(num, currDiv, divs):
  if num == 1:
    return divs
  while True:
    currDiv += 1
    if num % currDiv == 0:
      if prime(currDiv):
        currPow = 0
        while num % currDiv == 0:
          currPow += 1
          num /= currDiv
        divs *= (currPow + 1)
        break
  return divsCore(num, currDiv, divs)

def divs(num):
  return divsCore(num, 1, 1)

def triDivs():
  i = 1
  num = 1
  while True:
    if divs(num) > 500:
      print(num)
      break
    i += 1
    num += i

triDivs()
