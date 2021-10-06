"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

n = int(input())
groups = defaultdict(list)
for _ in range(n):
    s = input().strip()
    groups[s[0] + s[-1]].append(''.join(sorted(s)))
count = 0
for val in groups.values():
    count += len(set(val))
print(count)
