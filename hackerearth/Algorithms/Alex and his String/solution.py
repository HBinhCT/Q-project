"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from heapq import heapreplace, heappop, heapify

s = input().strip()
k = int(input())
x = ''
temp = list(s[:k])
heapify(temp)
for c in s[k:]:
    x += heapreplace(temp, c)
while temp:
    x += heappop(temp)
print(x)
