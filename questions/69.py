def primes_upto(limit):
    prime = [True] * limit
    for n in range(2, limit):
        if prime[n]:
            yield n # n is a prime
            for c in range(n*n, limit, n):
                prime[c] = False  # mark composites


primes = list(primes_upto(542))

n = 1
for p in primes:
    if n*p < 1000000:
        n *= p
    else:
        break

print(n)
