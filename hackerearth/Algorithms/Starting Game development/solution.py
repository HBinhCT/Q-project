"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_right

n, m, q = map(int, input().strip().split())
levels = []
for _ in range(n):
    levels.append(list(map(int, input().strip().split())))
for _ in range(q):
    strength = list(map(int, input().strip().split()))
    lvl = []
    ans = float('inf')
    for i in range(n):
        j = bisect_right(levels[i], strength[i])
        j -= (j == m)
        lvl.append(j)
    for i in range(n):
        temp = 0
        if levels[i][lvl[i]] > strength[i]:
            temp = lvl[i]
        else:
            temp = lvl[i] + 1
        ans = min(temp, ans)
    print(ans)
