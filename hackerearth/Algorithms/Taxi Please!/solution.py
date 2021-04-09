"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from heapq import heappop, heappush

n, m = map(int, input().strip().split())
assignments = [-1] * n
occupied = []
taxis = []
for i in range(1, m + 1):
    heappush(taxis, i)
users = []
for i in range(n):
    s, j = map(int, input().strip().split())
    heappush(users, (s, i, j))
while users:
    s, i, j = heappop(users)
    while occupied:
        d, idx = heappop(occupied)
        if d > s:
            heappush(occupied, (d, idx))
            break
        heappush(taxis, idx)
    if taxis:
        idx = heappop(taxis)
        assignments[i] = idx
        heappush(occupied, (s + j, idx))
print(*assignments)
