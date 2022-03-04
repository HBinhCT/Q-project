"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict
from math import gcd

mod = 1000000007
n = int(input())
a = list(map(int, input().strip().split()))
dp = [defaultdict(int) for _ in range(n)]
dp[0][a[0]] = 1
for i in range(1, n):
    dp[i][a[i]] = 1
    for j in range(i):
        if a[i] > a[j]:
            for k in dp[j]:
                g = gcd(a[i], k)
                dp[i][g] += dp[j][k]
                dp[i][g] %= mod
ans = 0
for subseq in dp:
    ans += subseq[1]
    ans %= mod
print(ans)
