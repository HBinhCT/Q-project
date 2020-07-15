"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

n = int(input())
a = list(map(int, input().strip().split()))
m = int(input())
c = list(map(int, input().strip().split()))
counts = defaultdict(lambda: 0)
for i in a:
    for j in c:
        counts[j - i] += 1
b = []
for k, v in counts.items():
    if v == n:
        b.append(k)
print(*sorted(b))
