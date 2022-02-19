"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_right

n = int(input())
a = list(map(int, input().strip().split()))
a.sort()
ln = len(a)
min_rm = float('inf')
for i in range(ln):
    j = bisect_right(a, 3 * a[i])
    if j > i:
        min_rm = min(min_rm, ln - (j - i))
print(min_rm)
