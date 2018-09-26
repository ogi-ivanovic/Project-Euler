def sumDigits(num):
    sum = 0
    num = str(num)
    length = len(num)
    for i in range(length):
        sum += int(num[i])
    return sum

def addFractTwo(num, fract):
    addedFract = [0, 0]
    addedFract[0] = num * fract[1] + fract[0]
    addedFract[1] = fract[1]
    return addedFract


seq = [1]
for k in range(1, 34):
    seq = seq + [2*k, 1, 1]
seq = seq[:99]

partialSum = 2
print(seq)
fract = [1, 1]
i = 98

while i > 0:
    fract = addFractTwo(seq[i], fract)
    fract = fract[::-1]

    i -= 1

fract = fract[::-1]
numerator = addFractTwo(2, fract)[0]
print(sumDigits(numerator))
