"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys

n, q = map(int, sys.stdin.readline().strip().split())
a = set(map(int, sys.stdin.readline().strip().split()))
for _ in range(q):
    x = int(sys.stdin.readline())
    print('YES' if x in a else 'NO')
