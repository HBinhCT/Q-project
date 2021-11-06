"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import re
from sys import stdin

for line in stdin.readlines():
    if '//' in line:
        blocks = re.split('//', line)
        blocks[0] = re.sub('->', '.', blocks[0])
        print('//'.join(blocks))
    else:
        print(re.sub('->', '.', line))
