"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import math

n = int(input())
a = map(int, input().strip().split())
s = 0
for i in a:
    s += math.log10(i)
print(int(10 ** (s / n)) + 1)
