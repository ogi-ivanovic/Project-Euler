primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def hamming(n):
    h = 1
    nums = [1]
    while nums:
        newnums = []
        for p in primes:
            for num in nums:
                if p*num <= n:
                    newnums.append(p*num)
        nums = list(dict.fromkeys(newnums))
        h += len(nums)
    return h


print(hamming(1000000000))
