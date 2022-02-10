"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
q = []
for _ in range(t):
    n = int(input())
    q.append(n)
ln = max(q) + 1
dp = [False] * ln
dp[1] = True
dp[4] = True
for i in range(10, ln):
    k = i
    while k > 0:
        k, r = divmod(k, 10)
        rr = r * r
        if rr < i:
            dp[i] |= dp[i - rr]
        if dp[i]:
            break
for n in q:
    print('Yes' if dp[n] else 'No')
