"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, d, y = map(int, input().strip().split())
a = map(int, input().strip().split())
print((max(a) + y * (d - 1) + d - 1) // d)
