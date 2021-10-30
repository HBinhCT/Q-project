"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from string import ascii_lowercase

tc = int(input())
for _ in range(tc):
    n = int(input())
    s = input()
    t = input()
    diff = 0
    for c in ascii_lowercase:
        diff += abs(s.count(c) - t.count(c))
    if diff == 0 or diff == 2:
        print('YES')
    else:
        print('NO')
