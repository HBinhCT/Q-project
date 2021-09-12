"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_left

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    c = sorted(zip(a, b))
    subsets = []
    for _, x in c:
        idx = bisect_left(subsets, x)
        subsets[idx: idx + 1] = [x]
    print(len(subsets))
