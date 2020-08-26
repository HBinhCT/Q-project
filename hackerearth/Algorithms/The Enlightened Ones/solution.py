"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect

n, k = map(int, input().strip().split())
positions = list(map(int, input().strip().split()))
positions.sort()
low, high = 0, positions[-1] - positions[0]
while low < high:
    mid = (low + high) // 2
    available = k
    i = 0
    is_solve = True
    while i < n:
        available -= 1
        if available < 0:
            is_solve = False
            break
        i = bisect(positions, positions[i] + mid * 2)
    if is_solve:
        high = mid
    else:
        low = mid + 1
print(low)
