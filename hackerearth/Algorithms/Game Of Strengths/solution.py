"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
mod = 1000000007
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().strip().split()))
    s = a[0]
    op = 0
    for i in range(1, n):
        x = a[i]
        op += x * i - s
        op %= mod
        s += x
    print(op * a[-1] % 1000000007)
