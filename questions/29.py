numbers = []

for a in range(2, 101):
    for b in range(2, 101):
        numbers.append(a**b)
numbers.sort()

new = []

length = len(numbers)
number = 0
for i in range(length):
    if numbers[i] == number:
        continue
    number = numbers[i]
    new.append(numbers[i])
print(len(new))
