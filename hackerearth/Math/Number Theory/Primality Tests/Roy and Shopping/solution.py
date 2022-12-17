def sieve_eratosthenes(x):
    size = x + 1
    sieve = bytearray(b'\x01' * size)
    sieve[0] = 0
    sieve[1] = 0
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, size, i):
                sieve[j] = 0
    ps = [i for i in range(2, size) if sieve[i] == 1]
    return sieve, ps


n = int(input())
products = []
mx = 0
for _ in range(n):
    r = int(input())
    products.append(r)
    mx = max(mx, r)
idxes, primes = sieve_eratosthenes(mx)
cache = {}
for r in products:
    if idxes[r]:
        print(0)
        continue
    if r in cache:
        print(cache[r])
        continue
    for p in primes:
        if not r % p:
            cache[r] = r - p
            print(cache[r])
            break
