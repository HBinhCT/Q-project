"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from math import gcd

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().strip().split())
    e = (a + b) // gcd(a, b)
    if e > n:
        e = n + 1
    print((2 * n + 3 - e) * e // 2)
