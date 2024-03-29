"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, k = map(int, input().strip().split())
digits = input().strip()
ln = len(digits)
dp = {}
for i in range(k + 1):
    dp[-1, i] = 1
for i in range(ln):
    dp[i, 0] = 1
    mul = 1 + (digits[i] != '0' and digits[i] != '9')
    for j in range(1, k + 1):
        dp[i, j] = (dp[i - 1, j] + dp[i - 1, j - 1] * mul) % 1000000007
print(dp[ln - 1, k] - 1)
