def addToOne(an):
  an[0] += an[1]
  return an

count = 0
an = [3, 2]
for i in range(2, 1001):
  an = addToOne(an)
  temp = an[0]
  an[0] = an[1]
  an[1] = temp
  an = addToOne(an)
  if len(str(an[0])) > len(str(an[1])):
    count += 1

print(count)
