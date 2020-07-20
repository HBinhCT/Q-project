"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys

n = int(sys.stdin.readline())
ans = 0
for _ in range(n):
    wh = tuple(map(int, sys.stdin.readline().strip().split()))
    ans += int(1.6 <= max(wh) / min(wh) <= 1.7)
print(ans)
