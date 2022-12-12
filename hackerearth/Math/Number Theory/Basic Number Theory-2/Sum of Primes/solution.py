from itertools import accumulate, chain, compress, zip_longest
from sys import stdin


def get_primes(num):
    zero = bytearray([False])
    length = num // 3 + (num % 6 == 2)
    sieve = bytearray([True]) * length
    sieve[0] = False
    for i in range(1, int(num ** 0.5) // 3 + 1):
        if sieve[i]:
            x = 3 * i + 1 | 1
            y = x * 2
            z = x * x
            start = (z + 4 * x - y * (i & 1)) // 3
            sieve[z // 3:: y] = zero * ((length - z // 3 - 1) // y + 1)
            sieve[start:: y] = zero * ((length - start - 1) // y + 1)
    res = [2, 3]
    poss = chain.from_iterable(zip_longest(*(range(i, num, 6) for i in (1, 5))))
    res.extend(compress(poss, sieve))
    return res


n = int(stdin.readline())
size = 0
lines = []
for _ in range(n):
    l, r = map(int, stdin.readline().strip().split())
    lines.append((l, r))
    size = max(size, r)
size += 1
primes = get_primes(size)
fx = [0] * size
for p in primes:
    fx[p] = p
fx = list(accumulate(fx))
for l, r in lines:
    print(fx[r] - fx[l - 1])
