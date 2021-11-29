"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from math import ceil, sqrt

t = int(input())
for _ in range(t):
    n, p = map(int, input().strip().split())
    x = list(map(int, input().strip().split()))
    y = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    if sum(a) < p:
        print(-1)
    else:
        circles = []
        for i in range(n):
            d = x[i] ** 2 + y[i] ** 2
            circles.append((d, a[i]))
        circles.sort()
        sum_val = 0
        for d, v in circles:
            sum_val += v
            if sum_val > p:
                print(ceil(sqrt(d)))
                break
