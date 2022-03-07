"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)

n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))


@lru_cache(None)
def dp(i, j, arr):
    if i == j:
        return True
    for x in range(i + 1, min(n, i + k + 1)):
        for y in range(j - 1, max(-1, j - k - 1), -1):
            if x <= y and arr[x] == arr[y] and dp(x, y, arr):
                return True
    return False


print('YES' if a[0] == a[n - 1] and dp(0, n - 1, tuple(a)) == 1 else 'NO')
