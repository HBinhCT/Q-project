"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from itertools import accumulate


def check(x, ln, arr):
    for i in range(x, ln + 1):
        if arr[i] - arr[i - x] >= 0:
            return True
    return False


def count(x, ln, arr):
    res = 0
    for i in range(x, ln + 1):
        if arr[i] - arr[i - x] >= 0:
            res += 1
    return res


n = int(input())
a = list(map(int, input().strip().split()))
sums = [0] + list(accumulate(a))
low = 1
high = n
ans = -1
while low <= high:
    mid = (low + high) // 2
    if check(mid, n, sums):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
if ans == -1:
    print(-1)
else:
    print(ans, count(ans, n, sums))
