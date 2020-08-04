"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
q = int(sys.stdin.readline())
a.sort()
b = [a[0]] * n
total = a[0]
for i in range(1, n):
    total += a[i]
    b[i] = total / (i + 1)
# for k in map(int, sys.stdin):
for _ in range(q):
    k = int(sys.stdin.readline())
    print(bisect_left(b, k))
