mod = 1000000007


def sieve(size):
    primes = [False, False] + [True] * (size - 1)
    for i in range(2, int(size ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, size + 1, i):
                primes[j] = False
    return [i for i, x in enumerate(primes) if x]


n = int(input())
if n == 1:
    print(0)
else:
    ans = 0
    for idx in sieve(2 * n):
        if idx < n - 1:
            ans += idx + 1
        else:
            ans += 2 * n - idx - 1
    print(ans % mod)
