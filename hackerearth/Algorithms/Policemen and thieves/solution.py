"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().strip().split())
    count = 0
    for _ in range(n):
        row = sys.stdin.readline().strip().split()
        polices = deque([])
        thieves = deque([])
        for i, v in enumerate(row):
            if v == 'P':
                polices.append(i)
            else:
                thieves.append(i)
        while polices and thieves:
            if abs(polices[0] - thieves[0]) <= k:
                count += 1
                polices.popleft()
                thieves.popleft()
            else:
                if polices[0] < thieves[0]:
                    polices.popleft()
                else:
                    thieves.popleft()
    print(count)
