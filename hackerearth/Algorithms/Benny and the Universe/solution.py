"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque, defaultdict

n, q = map(int, input().strip().split())
d = sorted(map(int, input().strip().split()))
t = d[0]
dist = [1000000000 for _ in range(t)]
dist[0] = 0
unvisited = set(range(t))
while unvisited:
    next_visit = min(unvisited, key=lambda i: dist[i])
    unvisited.remove(next_visit)
    for spacecraft in d:
        idx = (next_visit + spacecraft) % t
        if dist[idx] > dist[next_visit] + spacecraft:
            dist[idx] = dist[next_visit] + spacecraft
for _ in range(q):
    x = int(input())
    print('YES' if dist[x % t] <= x else 'NO')
