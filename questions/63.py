def digits(num):
    return len(str(num))

count = 0
for base in range(1, 10):
    n = 1
    while True:
        numDigits = digits(base ** n)

        if numDigits == n:
            count += 1
        if numDigits < n:
            break

        n += 1

print(count)
