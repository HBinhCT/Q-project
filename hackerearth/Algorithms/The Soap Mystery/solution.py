"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from collections import defaultdict

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
q = int(sys.stdin.readline())
lines = list(map(int, sys.stdin.readlines()))
size = max(lines)
counter = defaultdict(lambda: 0)
for i in a:
    counter[i + 1] += 1
for i in range(1, size + 1):
    counter[i] += counter[i - 1]
for m in lines:
    print(counter[m])
