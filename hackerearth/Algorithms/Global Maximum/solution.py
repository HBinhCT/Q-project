"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())


def check(arr, m_element, mid_val):
    count = 1
    i = 0
    ln = len(arr)
    while count < m_element:
        next_val = arr[i] + mid_val
        left = i + 1
        right = ln - 1
        res = -1
        while left <= right:
            middle = (left + right) // 2
            if arr[middle] >= next_val:
                res = middle
                right = middle - 1
            else:
                left = middle + 1
        if res == -1:
            return False
        i = res
        count += 1
    return count == m


low = 0
high = max(a) - min(a)
ans = -1
while low <= high:
    mid = (low + high) // 2
    if check(a, m, mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)
