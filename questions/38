def pandigital(n):
    n = str(n)
    if len(n) != 9:
        return False
    digits = [0]*10
    for num in n:
        num = int(num)
        digits[num] += 1
    for i in range(1, 10):
        if digits[i] != 1:
            return False
    return True

for i in range(9999, 9000, -1):
    n = int(str(i) + str(i * 2))
    if pandigital(n):
        print(n)
        break
