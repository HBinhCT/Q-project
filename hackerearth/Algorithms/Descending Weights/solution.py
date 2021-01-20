"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

n, k = map(int, input().strip().split())
a = map(int, input().strip().split())
bucket = defaultdict(list)
for i in a:
    bucket[i % k].append(i)
for key in sorted(bucket.keys(), reverse=True):
    print(*sorted(bucket[key]), end=' ')
