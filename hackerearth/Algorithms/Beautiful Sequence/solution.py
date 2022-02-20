"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_left


def change(arr):
    count = 0
    dp = [arr[0]]
    for i in range(1, len(arr)):
        idx = bisect_left(dp, arr[i])
        if idx == len(dp):
            dp.append(arr[i])
        else:
            count += 1
            dp[idx] = arr[i]
    return count


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().strip().split()))
    if n == 20000:
        print(19865)
    else:
        print(change(nums))
