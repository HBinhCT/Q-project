"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import math
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b, c, k = map(int, sys.stdin.readline().strip().split())
    if a == 0:
        x1 = x2 = (k - c) / b
    else:
        c = c - k
        delta = b * b - 4 * a * c
        if delta < 0:
            x1 = x2 = 0
        else:
            x1 = math.ceil((-b + delta ** .5) / (2 * a))
            x2 = math.ceil((-b - delta ** .5) / (2 * a))
    if x1 <= 0 and x2 <= 0:
        print(0)
    else:
        if x2 >= x1 and x1 < 0:
            print(x2)
        else:
            print(x1)
