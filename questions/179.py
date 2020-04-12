nums = [0] * 10000001

for i in range(2, 5000001):
    for j in range(2 * i, 10000001, i):
        nums[j] += 1

d = 0
for i in range(2, 10000000):
    if nums[i] == nums[i+1]:
        d += 1

print(d)
