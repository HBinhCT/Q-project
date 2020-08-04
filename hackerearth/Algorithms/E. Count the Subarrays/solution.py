"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    ans = 0
    if a[0] > k or a[0] < -k:
        ans += 1
    for i in range(1, n):
        a[i] += a[i - 1]
        if a[i] > k or a[i] < -k:
            ans += 1
    a = sorted(a)
    for i in range(n):
        ans += n - bisect(a, a[i] + k)
    print(ans)
