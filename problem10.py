import math

N = 2000000
primes = range(2,N)

maxNum = int(math.ceil(math.sqrt(N)))

for c in range(2,maxNum):
    first = True
    for count, prime in enumerate(primes):
        if prime%c==0:
            if first:
                first = False
            else:
                del primes[count]
                # primes.remove(prime)

print(sum(primes))
