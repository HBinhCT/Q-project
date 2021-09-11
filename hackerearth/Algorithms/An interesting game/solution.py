"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from queue import PriorityQueue
import numpy

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    sb = sum(b)
    pre = sorted(zip(b, numpy.add(a, b)))
    q = PriorityQueue()
    q.put(-pre[0][-1])
    ans = 0
    for i in range(0, n, 2):
        ans -= q.get()
        if i + 1 < n:
            q.put(-pre[i + 1][-1])
        if i + 2 < n:
            q.put(-pre[i + 2][-1])
    print(ans - sb)
