"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_left

n = int(input())
a = sorted(list(map(int, input().strip().split())))
q = int(input())
for _ in range(q):
    m = int(input())
    print(bisect_left(a, m))
