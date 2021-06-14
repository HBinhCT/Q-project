"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from collections import defaultdict

sys.setrecursionlimit(1000000000)  # 10 ** 9


def sum_all(start, pre_sum, pre_w, dp, adjacency, seen):
    mod = 1000000007
    global ans
    ans += dp[start]
    ans %= mod
    seen[start] = 1
    total = 0
    for y, w in adjacency[start]:
        if not seen[y]:
            dp[y] += (w * pre_sum + w) % mod
            dp[y] %= mod
            res = sum_all(y, dp[y], w, dp, adjacency, seen)
            total += res
            total %= mod
            pre_sum += res
            pre_sum %= mod
    return (total * pre_w + pre_w) % mod


n = int(input())
tree = defaultdict(list)
for _ in range(n - 1):
    u, v, c = map(int, input().strip().split())
    u -= 1
    v -= 1
    tree[u].append((v, c))
    tree[v].append((u, c))
ans = 0
sum_all(0, 0, 0, [0] * n, tree, [False] * n)
print(ans)
