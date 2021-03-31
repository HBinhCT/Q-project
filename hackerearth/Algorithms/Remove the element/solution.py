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
    n = int(input())
    a = sorted(map(int, input().strip().split()), reverse=True)
    total = 0
    prod = 1
    for i, x in enumerate(a):
        prod = prod * (i + 1) % mod
        total = (total + x * prod) % mod
    print(total)
