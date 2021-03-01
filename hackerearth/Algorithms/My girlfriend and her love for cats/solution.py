"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import numpy

n = int(input())
s = numpy.array(sorted(map(int, input().strip().split())))
c = numpy.array(sorted(map(int, input().strip().split())))
print(sum(s * c))
