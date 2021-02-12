"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import re

t = int(input())
for _ in range(t):
    s = input().strip()
    r = re.sub(r'(.)\1+', r'\1', s)
    print(r)
