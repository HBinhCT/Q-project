from collections import Counter
from sys import stdin

m, n = map(int, stdin.readline().strip().split())
x = map(int, stdin.readline().strip().split())
counter_prices = Counter(x)
remaining = n
ans = 0
k = max(counter_prices)
while k > 0 and remaining > 0:
    amount = min(counter_prices[k], remaining)
    ans += amount * k
    counter_prices[k - 1] += amount
    k -= 1
    remaining -= amount
print(ans)
