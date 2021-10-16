"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from math import ceil, sqrt

t = int(input())
for _ in range(t):
    n = int(input())
    print(int(-2 + ceil(2 * (sqrt(1 + n)))))
