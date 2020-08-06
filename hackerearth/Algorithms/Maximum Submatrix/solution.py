"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys

n, m = map(int, sys.stdin.readline().strip().split())
x = int(sys.stdin.readline())
a = [[0] * (m + 2)]
for _ in range(n):
    a.append([0] + list(map(int, sys.stdin.readline().strip().split())) + [0])
    # line = [0]
    # for _ in range(m):
    #     line.append(int(sys.stdin.readline()))
    # line.append(0)
    # a.append(line)
a.append([0] * (m + 2))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        a[i][j] = a[i][j - 1] + a[i][j]
    for j in range(1, m + 1):
        a[i][j] = a[i - 1][j] + a[i][j]
low = 0
high = min(n, m)
while low < high:
    mid = (low + high + 1) // 2
    check = False
    for i in range(mid, n + 1):
        if check:
            break
        for j in range(mid, m + 1):
            if check:
                break
            val = a[i][j] - a[i - mid][j] - a[i][j - mid] + a[i - mid][j - mid]
            if val <= x:
                check = True
    if check:
        low = mid
    else:
        high = mid - 1
print(low * low)
