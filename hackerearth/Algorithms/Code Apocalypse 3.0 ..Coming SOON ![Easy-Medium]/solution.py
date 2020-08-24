"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m, x, y = map(int, sys.stdin.readline().strip().split())
    ans = min((y * n + m) // (x + y), n)
    print(ans)
