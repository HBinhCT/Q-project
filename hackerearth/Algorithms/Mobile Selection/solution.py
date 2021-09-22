"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect

OSIds = {
    'windows': 0,
    'android': 1,
    'ios': 2,
}
RAMIds = {
    '2': 0,
    '4': 1,
    '8': 2,
}
MemoryIds = {
    '32': 0,
    '64': 1,
}

n = int(input())
prices = {-1: -1}
phones = []
for _ in range(n):
    s, a, b, c, d = input().strip().split()
    c = int(c)
    d = int(d)
    phones.append((s, a, b, c, d)),
    prices[c] = 0
sorted_prices = sorted(prices)
for i, v in enumerate(sorted_prices):
    prices[v] = i
ratings = [[[[-1] * (n + 1) for _ in MemoryIds] for _ in RAMIds] for _ in OSIds]
for s, a, b, c, d in phones:
    r = ratings[OSIds[s]][RAMIds[a]][MemoryIds[b]]
    x = prices[c]
    while x <= n:
        r[x] = max(r[x], d)
        x += x & -x
q = int(input())
for _ in range(q):
    h, e, f, g = input().strip().split()
    v = ratings[OSIds[h]][RAMIds[e]][MemoryIds[f]]
    g = int(g)
    x = bisect(sorted_prices, g) - 1
    y = -1
    while x > 0:
        y = max(y, v[x])
        x -= x & -x
    print(y)
