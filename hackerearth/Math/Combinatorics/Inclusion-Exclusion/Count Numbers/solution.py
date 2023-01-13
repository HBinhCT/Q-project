from functools import reduce
from itertools import combinations
from operator import mul

k, t = map(int, input().strip().split())
primes = list(map(int, input().strip().split()))
for _ in range(t):
    a, b = map(int, input().strip().split())
    ans = 0
    for i in range(1, k + 1):
        for j in combinations(primes, i):
            x = b // reduce(mul, j) - (a - 1) // reduce(mul, j)
            if i & 1:
                ans += x
            else:
                ans -= x
    print(ans)
