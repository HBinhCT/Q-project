"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
h = [list(map(int, input().strip().split())) for _ in range(n)]
v = [list(map(int, input().strip().split())) for _ in range(n)]
power = [[0] * (n + 1) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n)]
for i in range(n):
    total = sum(v[i])
    power[i][-1] = total
    if i:
        power[i][-1] += power[i - 1][-1]
    for j in range(n - 1, -1, -1):
        dp[i][j] = h[i][j] - v[i][j] + dp[i][j + 1]
        firepower = total + dp[i][j]
        if i:
            firepower += power[i - 1][j]
        power[i][j] = max(firepower, power[i][j + 1])
print(power[-1][0])
