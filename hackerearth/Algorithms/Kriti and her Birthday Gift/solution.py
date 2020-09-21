"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
lookup = {}
for i in range(1, n + 1):
    string = sys.stdin.readline().strip()
    if string in lookup:
        lookup[string].append(i)
    else:
        lookup[string] = [i]
q = int(sys.stdin.readline())
for _ in range(q):
    l, r, s = sys.stdin.readline().strip().split()
    if s in lookup:
        range_list = lookup[s]
        left_position = bisect_left(range_list, int(l))
        right_position = bisect_right(range_list, int(r))
        print(right_position - left_position)
    else:
        print(0)
