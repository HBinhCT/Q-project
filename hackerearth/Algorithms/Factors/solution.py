"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
mod = 1000000007
t = int(input())
for _ in range(t):
    ln = int(input())
    a = sorted(map(int, input().strip().split()))
    b = sorted(map(int, input().strip().split()), reverse=True)
    m = n = 1
    for a, b in zip(a, b):
        m *= (a + b + 1)
        m %= mod
        n *= (a + 1) * (b + 1)
        n %= mod
    print(m, n)
