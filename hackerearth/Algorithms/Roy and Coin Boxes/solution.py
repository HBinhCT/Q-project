"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_left

n = int(input())
m = int(input())
counter = [0] * n
for _ in range(m):
    l, r = map(lambda x: int(x) - 1, input().split())
    counter[l] += 1
    if r + 1 < n:
        counter[r + 1] -= 1
boxes = [0] * n
boxes[0] = counter[0]
for i in range(1, n):
    boxes[i] = boxes[i - 1] + counter[i]
boxes.sort()
q = int(input())
for _ in range(q):
    x = int(input())
    print(n - bisect_left(boxes, x))
