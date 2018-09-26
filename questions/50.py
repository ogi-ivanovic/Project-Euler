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

nums = [0]*1000000
nums[0] = 1
nums[1] = 1
for i in range(2, 1000000):
  if nums[i] == 0 and prime(i):
    for j in range(i*2, 1000000, i):
      nums[j] = 1
primes = [2]
for i in range(3, 1000000, 2):
  if nums[i] == 0:
    primes.append(i)



def conseqCore(num, length, currSum, start, curr, overBefore):
  if currSum == num:
    return length
  if currSum < num:
    if overBefore:
      return 0
    else:
      return conseqCore(num, length + 1, currSum + primes[curr], start,curr + 1, overBefore)
  return conseqCore(num, length - 1, currSum - primes[start], start + 1, curr, True)


def conseq(num):
  return conseqCore(num, 0, 0, 0, 0, False)

max = 0
maxPrime = 0  
for prime in primes:
  print(prime)
  x = conseq(prime)
  if x > max:
    max = x
    maxPrime = prime

print(maxPrime)
