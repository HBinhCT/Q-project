"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    ans = n * (n + 1) // 2
    counter = defaultdict(int)
    j = -1
    for i, x in enumerate(a):
        counter[x] += 1
        while counter[x] >= k:
            j += 1
            counter[a[j]] -= 1
        ans -= i - j
    print(ans)
