"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
r, c = map(int, input().strip().split())
cells = []
for _ in range(r):
    cells.append(list(map(int, input().strip().split())))
dp = [[0] * (c + 1) for _ in range(r + 1)]
for i in range(1, r + 1):
    for j in range(1, c + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + cells[i - 1][j - 1]
q = int(input())
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().strip().split())
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])
