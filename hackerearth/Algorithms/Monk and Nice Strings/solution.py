"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import insort

n = int(input())
a = []
for _ in range(n):
    s = input().strip()
    insort(a, s)
    print(a.index(s))
