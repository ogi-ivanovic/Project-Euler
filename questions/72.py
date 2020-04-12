nums = [0] * 1000001
for i in range(1, 1000001):
  nums[i] = i - 1
  
for i in range(2, 500001):
  for j in range(2*i, 1000001, i):
    nums[j] -= nums[i]

d = 0
for i in range(2, 1000001):
  d += nums[i]

print(d)
