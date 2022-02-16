"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
sequence = list(map(int, input().strip().split()))
dp = [1] * t
for i in range(1, t):
    for j in range(i - 1, -1, -1):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(bin(max(dp))[2:])
