"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from itertools import accumulate

t = int(input())
q = []
for _ in range(t):
    n = int(input())
    q.append(n)
ln = max(q)
dp = [1] * (ln + 1)
for i in range(2, ln // 2 + 1):
    for j in range(2 * i, ln + 1, i):
        dp[j] += 1
dp = [0, 0] + list(accumulate(dp[2:]))
for n in q:
    print(dp[n])
