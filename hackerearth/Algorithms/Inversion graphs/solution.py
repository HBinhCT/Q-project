"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_left

n = int(input())
a = list(map(int, input().strip().split()))
res = []
for x in a[::-1]:
    i = bisect_left(res, x)
    if i == len(res):
        res.append(x)
    else:
        res[i] = x
print(len(res))
