"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys

n, k = map(int, sys.stdin.readline().strip().split())
a = sorted(map(int, sys.stdin.readline().strip().split()))


def count_pairs(arr, x):
    ln = len(arr)
    ans = 0
    j = 0
    for i in range(ln):
        while j < ln and arr[j] - arr[i] <= x:
            j += 1
        ans += j - i - 1
    return ans


low, high = 0, a[-1] - a[0] + 1
while low < high:
    mid = (low + high) // 2
    if count_pairs(a, mid) >= k:
        high = mid
    else:
        low = mid + 1
print(low)
