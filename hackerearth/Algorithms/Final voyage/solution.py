"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())


def calc(size, load, item_weights, item_values):
    dp = [[0] * (load + 1) for _ in range(size + 1)]
    for i in range(1, size + 1):
        for j in range(1, load + 1):
            if item_weights[i - 1] <= j:
                dp[i][j] = max(item_values[i - 1] + dp[i - 1][j - item_weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[size][load]


for _ in range(t):
    n = int(input())
    w = int(input())
    weights = []
    values = []
    if n > 0:
        weights = list(map(int, input().strip().split()))
    if w > 0:
        values = list(map(int, input().strip().split()))
    if n > 0 and w > 0:
        print(calc(n, w, weights, values))
    else:
        print(0)
