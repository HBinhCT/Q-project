"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect

t = int(input())
for _ in range(t):
    n, k, p = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    if n - k < p:
        print(-1)
    else:
        while True:
            index = bisect(a, p)
            if index == 0:
                break
            a = a[index:]
            p += index
        print(p)
