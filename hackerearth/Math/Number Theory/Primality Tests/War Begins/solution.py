from bisect import bisect_right


def sieve(size):
    is_primes = [False, False] + [True] * (size - 2)
    for i in range(2, int(size ** .5) + 1):
        if is_primes[i]:
            for j in range(i * i, size, i):
                is_primes[j] = False
    return [i for i, x in enumerate(is_primes) if x]


mod = 100000007
q = int(input())
m = 0
nums = []
for _ in range(q):
    n = int(input())
    nums.append(n)
    m = max(m, n)
primes = sieve(m + 1)
totals = [0] * (len(primes) + 1)
for i in range(1, len(primes)):
    totals[i + 1] = (totals[i] + primes[i] // 2) % mod
for n in nums:
    i = bisect_right(primes, n)
    print(totals[i])
