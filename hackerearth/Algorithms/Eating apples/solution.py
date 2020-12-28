"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

n = int(input())
d = defaultdict(list)
for i in range(n):
    x, y = map(int, input().strip().split())
    d[x].append((y, i))
out = [0 for i in range(n)]
count = 0
left = True
for k, v in sorted(d.items()):
    if left:
        for app, pos in sorted(v):
            out[pos] = count
            count += 1
    else:
        for app, pos in reversed(sorted(v)):
            out[pos] = count
            count += 1
    left = not left
print(*out, sep='\n')
