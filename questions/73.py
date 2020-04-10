import math

def relprim(x):
    start = math.floor(x / 3) + 1
    if x % 2 == 0:
        end = math.floor(x / 2)
    else:
        end = math.floor(x / 2) + 1
    prims = 0
    for i in range(start, end):
        if math.gcd(x, i) == 1:
            prims += 1

    return prims

inrange = 0
for i in range(4, 12001):
    inrange += relprim(i)

print(inrange)
