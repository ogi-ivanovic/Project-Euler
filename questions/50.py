def reverse(n):
  rev = 0
  while n > 0:
    rev *= 10
    j = n % 10
    rev += j
    n =(n - j)/10
  return int(rev)

def addRev(n):
  return n + reverse(n)

def palindrome(n):
  n = str(n)
  le = len(n)
  length = int(le/2)
  for i in range(length):
    if n[i] != n[le - i - 1]:
      return False
  return True

def lychrel(n, steps):
  if steps == 50:
    return True
  n = addRev(n)
  steps += 1
  if palindrome(n):
    return False
  return lychrel(n, steps)

count = 0 
for i in range(1, 10000):
  if lychrel(i, 0):
    count += 1
print(count)
