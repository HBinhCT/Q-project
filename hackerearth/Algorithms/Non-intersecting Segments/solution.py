"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect

n = int(input())
segments1 = []
segments2 = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().strip().split())
    segments1.append((x1, x2))
    segments2.append((y1, y2))
if n == 1:
    print(1)
else:
    segments1.sort()
    if segments1[0][0] == segments1[1][0]:
        segments1 = segments2
        segments1.sort()
    ans = [segments1[0][1]]
    for i in range(1, n):
        idx = bisect(ans, segments1[i][1])
        if idx == len(ans):
            ans.append(segments1[i][1])
        else:
            ans[idx] = segments1[i][1]
    print(len(ans))
