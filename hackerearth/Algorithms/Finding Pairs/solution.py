"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int, input().strip().split())
    print(sum(i * (i + 1) // 2 for i in Counter(a).values()))
