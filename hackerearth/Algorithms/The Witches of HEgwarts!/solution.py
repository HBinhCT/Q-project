"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())


def fn(x, dp):
    if x <= 1:
        return 0
    if x in dp:
        return dp[x]
    opt1 = 1 + (x % 2) + fn(x // 2, dp)
    opt2 = 1 + (x % 3) + fn(x // 3, dp)
    dp[x] = min(opt1, opt2)
    return dp[x]


for _ in range(t):
    n = int(input())
    print(fn(n, {}))
