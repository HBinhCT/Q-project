"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from math import gcd
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    a, b = list(map(int, stdin.readline().strip().split()))
    c = gcd(a, b)
    print('No' if c & c - 1 else 'Yes')
