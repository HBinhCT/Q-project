"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import Counter

n = int(input())
a = map(int, input().strip().split())
k = int(input())
c = Counter(a)
print(min(filter(lambda x: x[1] == k, c.items()))[0])
