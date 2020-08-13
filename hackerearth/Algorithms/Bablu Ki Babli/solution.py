"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from bisect import bisect_left

n, q = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
x = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    a[i] += a[i - 1]
for i in range(q):
    print(bisect_left(a, x[i]) + 1)
