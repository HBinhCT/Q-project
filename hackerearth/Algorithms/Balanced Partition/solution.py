"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    houses = defaultdict(int)
    total = 0
    for _ in range(n):
        x, y, h = map(int, input().split())
        houses[y - x] += h
        total += h
    avg = total / 2
    i = 0
    for key in sorted(houses.keys()):
        i += houses[key]
        if i >= avg:
            print('YES' if i == avg or total == 2 * i - houses[key] else 'NO')
            break
