"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_left
from itertools import accumulate

n, q = map(int, input().split())
a = map(int, input().split())
m = list(map(int, input().split()))
totals = list(accumulate(a))
for i in range(q):
    print(bisect_left(totals, m[i]) + 1)
