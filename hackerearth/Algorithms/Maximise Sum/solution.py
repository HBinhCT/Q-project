"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = list(map(int, input().strip().split()))
dp = [0] * n
dp[0] = a[0]
dp[1] = max(a[0] + a[1], a[0] * a[1])
for i in range(2, n):
    dp[i] = max(dp[i - 1] + a[i], dp[i - 2] + a[i] * a[i - 1])
print(dp[-1])
