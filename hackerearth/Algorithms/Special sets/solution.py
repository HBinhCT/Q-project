"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from math import factorial

n = int(input())
left = 1
right = n
res = 0
while right >= left:
    res += factorial(right) // factorial(right - left)
    right -= 1
    left += 1
print(res % 1000000007)
