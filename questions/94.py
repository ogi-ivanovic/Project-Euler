import math

def is_square(integer):
    root = math.sqrt(integer)
    return integer == int(root + 0.5) ** 2

p = 0

for i in range(3, 333333333, 2):
    if is_square(3*i*i - 2*i - 1):
        p += 3*i + 1
    if is_square(3*i*i + 2*i - 1):
        p += 3*i - 1

print(p)
