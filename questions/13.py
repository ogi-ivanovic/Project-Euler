sum = 0

for i in range(100):
  x = input()
  x = int(x)
  sum += x

sum = str(sum)

answer = ' '
for i in range(10):
  answer = answer + sum[i]

print(answer)
