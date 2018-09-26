def levelSum(level):
  return 2*level + (level - 2)*2

def numLaminae(tiles):
  count = 0
  inn = 1
  while levelSum(inn + 2) <= tiles:
    level = inn + 2
    levSum = levelSum(level)
    while levSum <= tiles:
      count += 1
      level += 2
      levSum += levelSum(level)
    inn += 1
  return count

print(numLaminae(1000000))
