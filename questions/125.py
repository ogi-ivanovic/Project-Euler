from math import *

def reverse(x):
  x = str(x)
  rev = ''
  length = len(x)
  for i in range(length - 1, -1, -1):
    rev = rev + x[i]
  return rev

sqrSums = [0]*22362
for i in range(1, 22362):
  sqrSums[i] = sqrSums[i - 1] + i*i


def conseq(num):
  sum = 1
  lowerBound = 1
  upperBound = 1
  max = int(floor(sqrt(num)))
  while sum != num:
    if sum < num:
      upperBound += 1
      sum += upperBound * upperBound
    if sum > num: 
      sum -= lowerBound * lowerBound
      lowerBound += 1
    if upperBound > max:
      return False
  if upperBound > lowerBound:
    return True
  return False

pans = [2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, 1000):
  num = int(str(i) + reverse(i))
  pans.append(num)
  num = str(num)
  half = int(len(num)/2)
  for i in range(10):
    x = num[:half] + str(i) + num[half:]
    pans.append(int(x)) 

for i in range(1000, 10000):
  num = int(str(i) + reverse(i))
  pans.append(num)


pans = list(set(pans))

j = 0
sum = 0
for i in pans:
  print(j)
  j += 1
  if conseq(i):
    sum += i

print(sum)
