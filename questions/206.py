def fills_blanks(x):
    j = 1
    for i in range(0, 19, 2):
        if x[i] != str(j):
            return False
        j = (j + 1) % 10

    return True


for i in range(1414213570, 1000000000, -10):
    if fills_blanks(str(i*i)):
        print(i)
