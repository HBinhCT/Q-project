"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from itertools import accumulate
from sys import stdin

n, q = map(int, stdin.readline().strip().split())
a = list(map(int, stdin.readline().strip().split()))
b = list(map(int, stdin.readline().strip().split()))
for i in range(1, n, 2):
    a[i], b[i] = b[i], a[i]
a = list(accumulate(a))
b = list(accumulate(b))
for _ in range(q):
    t, l, r = map(int, stdin.readline().strip().split())
    if l == 1:
        print(a[r - 1] if t == 1 else b[r - 1])
    elif l % 2:
        print(a[r - 1] - a[l - 2] if t == 1 else b[r - 1] - b[l - 2])
    else:
        print(b[r - 1] - b[l - 2] if t == 1 else a[r - 1] - a[l - 2])
