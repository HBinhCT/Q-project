"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import Counter

n = int(input())
a = input().strip().split()
counter = Counter(a)
pairs = sum((i * (i - 1)) // 2 for i in counter.values() if i > 1)
print(pairs)
