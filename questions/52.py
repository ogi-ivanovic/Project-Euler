def sameDigits(num, mult):
  multNum = str(num * mult)
  num = str(num)
  if len(num) != len(multNum):
    return False
  digitsNum = [0]*10
  digitsMult = [0]*10
  for i in range(len(num)):
    dNum = int(num[i])
    dMult = int(multNum[i])
    digitsNum[dNum] += 1
    digitsMult[dMult] += 1
  return digitsNum == digitsMult

i = 1
while True:
  if sameDigits(i, 2) and sameDigits(i, 3) and sameDigits(i, 4) and sameDigits(i, 5) and sameDigits(i,6):
    print(i)
    break
  i += 1
