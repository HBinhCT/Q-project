"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from collections import Counter

n = int(sys.stdin.readline())
make_key = lambda x: ' '.join(sorted(x.strip().split()))
count = Counter(map(make_key, sys.stdin.readlines()))
print(list(count.values()).count(1))
