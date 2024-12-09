def sieve(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as True.
    # A value in prime[i] will be False if i is Not a prime, and True if i is a prime.
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False  # 0 and 1 are not primes
    
    p = 2
    while p * p <= n:  # Only check up to sqrt(n)
        if prime[p]:
            # Update all multiples of p to False
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(n + 1) if prime[p]]

n = 5000000
primes = sieve(n)
print(primes[10000])