"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import heapq

n, x = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
b = []
heapq.heapify(b)
for i in range(n):
    if a[i]:
        heapq.heappush(b, -a[i])
    else:
        if x >= len(b):
            b = []
            heapq.heapify(b)
        else:
            for j in range(x):
                heapq.heappop(b)
print(-sum(b))
