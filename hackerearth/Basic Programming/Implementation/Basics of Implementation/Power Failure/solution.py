from bisect import bisect_left, bisect_right

n = 100000
mod = 1000000007
is_primes = [True] * (n + 1)
is_primes[0] = is_primes[1] = False
for i in range(2, int(n**0.5) + 1):
    if is_primes[i]:
        for j in range(i * i, n + 1, i):
            is_primes[j] = False
primes = [i for i in range(n + 1) if is_primes[i]]
t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    volts = sorted(map(int, input().strip().split()), reverse=True)
    x = bisect_right(primes, m)
    ans = 1
    for i, v in enumerate(volts):
        y = bisect_left(primes, v)
        z = m - v + 1 - i - (x - y)
        if z <= 0:
            print(0)
            break
        ans = (ans * z) % mod
    else:
        print(ans)
