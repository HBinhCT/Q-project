"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import math

n = int(input())
res = []
for i in range(1, n - 1):
    if math.gcd(i, n) == 1:
        res.append(i)
print(max(res))
