def sieve(size):
    is_primes = [False, False] + [True] * (size - 2)
    for i in range(2, int(size ** .5) + 1):
        if is_primes[i]:
            for j in range(i * i, size, i):
                is_primes[j] = False
    return is_primes


def count_primes(size):
    primes = sieve(size)
    count = pp_count = 0
    prefix_sum = [0] * size
    for i in range(n + 1):
        if primes[i]:
            count += 1
        if primes[count]:  # that means i is Prime Prime
            pp_count += 1
        prefix_sum[i] = pp_count
    return prefix_sum


t = int(input())
lines = []
n = 0
for _ in range(t):
    l, r = map(int, input().strip().split())
    lines.append((l, r))
    n = max(n, r)
pp = count_primes(n + 1)
for l, r in lines:
    ans = pp[r] - pp[l - 1]
    print(ans)
