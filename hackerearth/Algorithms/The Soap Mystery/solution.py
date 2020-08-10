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
a.sort()
q = int(sys.stdin.readline())
for _ in range(q):
    m = int(sys.stdin.readline())
    print(bisect_left(a, m))
