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
    n = int(input())
    needs = defaultdict(int)
    for i in range(n):
        l, r, z = map(int, input().strip().split())
        needs[r] += z
    ans = 0
    needs = sorted(needs.items())
    total = 0
    for r, z in needs:
        total += z
        ans = max(ans, (total + r - 1) // r)
    print(ans)
