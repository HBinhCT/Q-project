"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_right

t = int(input())
a = list(map(int, input().strip().split()))
totals = [a[0]]
for i in range(1, t):
    totals.append(totals[i - 1] + a[i])
q = int(input())
for _ in range(q):
    target = int(input())
    index = bisect_right(totals, target)
    if index == 0:
        print(1)
    elif index == t and totals[index - 1] == target:
        print(index)
    elif index < t:
        print(index + int(totals[index - 1] != target))
    else:
        print(-1)
