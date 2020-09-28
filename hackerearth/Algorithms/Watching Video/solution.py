"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, d = map(int, input().strip().split())
x = list(map(int, input().strip().split()))
dp = [0] * len(x)
cache = 0
for i in range(n):
    cache += x[i]
    if cache >= d:
        dp[i], cache = divmod(cache, d)
play = cache = 0
for i in range(n):
    if dp[i]:
        play = max(play, i - cache)
    cache += dp[i]
print(play + 1)
