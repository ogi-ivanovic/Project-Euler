def digits(x):
    digits = []
    x = str(x)
    length= len(x)
    for i in range(length):
        digits.append(x[i])
    digits.sort()
    return digits

def isPerm(x, y):
    return digits(x) == digits(y)

cubes = []
for i in range(4600, 10000):
    cubes.append(i**3)

lengthCubes = len(cubes)

for a in range(lengthCubes - 4):
    for b in range(a + 1, lengthCubes - 3):
        if isPerm(cubes[a], cubes[b]):
            for c in range(b + 1, lengthCubes - 2):
                if isPerm(cubes[a], cubes[c]):
                    for d in range(c + 1, lengthCubes - 1):
                        if isPerm(cubes[a], cubes[d]):
                            for e in range(d + 1, lengthCubes):
                                if isPerm(cubes[a], cubes[e]):
                                    print(cubes[a])
