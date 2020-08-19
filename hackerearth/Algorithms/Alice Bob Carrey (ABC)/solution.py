"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from bisect import bisect_left
from itertools import accumulate

n = int(sys.stdin.readline())
a = map(int, sys.stdin.readline().strip().split())
q = int(sys.stdin.readline())
totals = list(accumulate(a))
for _ in range(q):
    x = int(sys.stdin.readline())
    i = bisect_left(totals, totals[-1] - x + 1)
    print('Bob' if i % 2 else 'Alice')
