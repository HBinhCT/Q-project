"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m = map(int, input().strip().split())
boxes = [0] * m
for _ in range(n):
    p, b = map(int, input().strip().split())
    boxes[b - 1] = max(p, boxes[b - 1])
print(sum(boxes))
