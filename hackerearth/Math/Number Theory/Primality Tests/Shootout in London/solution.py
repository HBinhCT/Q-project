def sieve(size):
    is_primes = [False, False] + [True] * (size - 2)
    for i in range(2, int(size ** .5) + 1):
        if is_primes[i]:
            for j in range(i * i, size, i):
                is_primes[j] = False
    return is_primes


n = int(input())
a = list(map(int, input().strip().split()))
primes = sieve(max(a) + 1)
nearest = -1
for i in range(n):
    if primes[a[i]]:
        nearest = i
        break
if nearest == -1:
    ans = [-1] * n
    print(*ans)
else:
    ans = [0] * n
    for i in range(nearest + 1):
        ans[i] = nearest + 1
    k = nearest
    for i in range(k + 1, n):
        if primes[a[i]]:
            ans[i] = i + 1
            nearest = i
            continue
        for j in range(i + 1, min(2 * i - nearest, n)):
            if primes[a[j]]:
                nearest = j
                break
        ans[i] = nearest + 1
    print(*ans)
