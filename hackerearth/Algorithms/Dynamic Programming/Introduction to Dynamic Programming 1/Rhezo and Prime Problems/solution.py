from itertools import accumulate

mx = 5000
is_primes = [False, False] + [True] * (mx - 1)
for i in range(2, int(mx ** .5) + 1):
    if is_primes[i]:
        for j in range(i * i, mx + 1, i):
            is_primes[j] = False
primes = [i for i in range(mx + 1) if is_primes[i]]
n = int(input())
a = list(map(int, input().strip().split()))
totals = list(accumulate(a, initial=0))
dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1]
    for j in primes:
        if j > i:
            break
        dp[i] = max(dp[i], dp[max(i - j - 1, 0)] + totals[i] - totals[i - j])
print(dp[n])
