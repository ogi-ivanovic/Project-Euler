from math import *

def wordValue(word):
    value = 0
    for letter in word:
        value += ord(letter) - ord('A') + 1
    return value

def triangleNumber(x):
    n = (-1 + sqrt(1 + 8*x))/2
    if n - int(n) == 0.0:
        return True
    return False

words = [...]

count = 0
for word in words:
    if triangleNumber(wordValue(word)):
        count += 1
print(count)
