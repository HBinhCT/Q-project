"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    s = 0
    pre = [0]
    for i in a:
        s = max(s + i, 0)
        pre.append(s)
    ans = mx = s = 0
    for i in range(n - 1, -1, -1):
        s = max(s + a[i], 0)
        mx = max(s, mx)
        ans = max(ans, mx + pre[i])
    print(ans)
