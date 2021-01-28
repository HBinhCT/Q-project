"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import functools
import operator

n = int(input())
a = map(int, input().strip().split())
print(1 if functools.reduce(operator.xor, a) else -1)
