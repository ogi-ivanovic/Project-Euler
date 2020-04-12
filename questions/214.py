nums = [0] * 40000001

for i in range(40000001):
    nums[i] = i - 1

for i in range(2, 20000001):
    for j in range(2*i, 40000001, i):
        nums[j] -= nums[i]

chains = [0] * 40000001
chains[1] = 1
chains[2] = 2
chains[3] = 3
s = 0
for i in range(4, 40000001):
    chains[i] = chains[nums[i]] + 1
    if nums[i] == i-1 and chains[i] == 25:
        s += i
print(s)
