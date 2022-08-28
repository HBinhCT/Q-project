from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate
from operator import mul
from sys import stdin


def get_primes(x):
    if x <= 2:
        return []
    nums = list(range(3, x, 2))
    top = len(nums)
    for num in nums:
        if num:
            bottom = (num * num - 3) // 2
            if bottom >= top:
                break
            nums[bottom::num] = [0] * -((bottom - top) // num)
    return [2] + [num for num in nums if num]


def get_danger_val(prime_list, cost):
    counts = defaultdict(lambda: 1)
    while cost > 1:
        if cost in prime_list:
            counts[cost] += 1
            break
        for prime in prime_list:
            if cost % prime == 0:
                counts[prime] += 1
                cost //= prime
                break
    return reduce(mul, counts.values(), 1)


n = int(stdin.readline())
prices = list(map(int, stdin.readline().strip().split()))
primes = set(get_primes(max(prices) + 1))
dangers = []
for i in prices:
    dangers.append(get_danger_val(primes, i))
same_dangers = set()
for k, v in Counter(dangers).items():
    if v > 1:
        same_dangers.add(k)
dp = dict()
for i in same_dangers:
    dp[i] = [0] * (n + 1)
for i, v in enumerate(dangers, 1):
    if v in same_dangers:
        dp[v][i] = 1
for i in dp:
    dp[i] = list(accumulate(dp[i]))
q = int(stdin.readline())
for _ in range(q):
    left, right = map(int, stdin.readline().strip().split())
    left -= 1
    cnt = 0
    for i in same_dangers:
        val = dp[i][right] - dp[i][left]
        if val > 1:
            cnt += val * (val - 1) // 2
    print(cnt)
