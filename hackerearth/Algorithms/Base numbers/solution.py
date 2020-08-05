"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import math
import sys


def search_lower(a, b, n):
    low = 1
    high = 1000000000  # 10**9
    val = n - math.log(a, b)
    ans = 0
    while high >= low:
        mid = (high + low) // 2
        x_log_x = mid * math.log(mid, b)
        if x_log_x < val:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


for line in sys.stdin.readlines():
    a, n, b = map(int, line.strip().split())
    x_lower = search_lower(a, b, n - 1)
    x_upper = search_lower(a, b, n)
    print(x_upper - x_lower)
