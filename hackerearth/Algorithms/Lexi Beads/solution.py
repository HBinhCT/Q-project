"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import re

n = int(input())
for _ in range(n):
    k, s = input().strip().split()
    k = int(k)
    if k > 1:
        print(''.join(sorted(s)))
    else:
        mc = min(s)
        pos = [m.start() for m in re.finditer(mc, s)]
        temp = s
        for i in pos:
            temp = min(temp, s[i:] + s[:i])
        print(temp)
