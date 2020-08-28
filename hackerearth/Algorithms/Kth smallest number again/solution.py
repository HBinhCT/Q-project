"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_left

t = int(input())
for _ in range(t):
    n, q = map(int, input().strip().split())
    ranges = []
    for _ in range(n):
        a, b = map(int, input().split())
        ranges.append([a, b])
    ranges.sort()
    final_range = [ranges[0]]
    j = 0
    for i in range(1, n):
        if ranges[i][0] <= final_range[j][1]:
            final_range[j][1] = max(ranges[i][1], final_range[j][1])
        else:
            final_range.append(ranges[i])
            j += 1
    total = 0
    prefix = []
    for r in final_range:
        total += r[1] - r[0] + 1
        prefix.append(total)
    for _ in range(q):
        k = int(input())
        if k > total:
            print(-1)
        else:
            index = bisect_left(prefix, k)
            if index:
                offset = k - prefix[index - 1] - 1
            else:
                offset = k - 1
            print(final_range[index][0] + offset)
