"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import Counter

mod = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    cnt = Counter(Counter(a).values())
    ans = 1
    for v in cnt.values():
        ans *= pow(2, v - 1, mod)
        ans %= mod
    print(ans)
