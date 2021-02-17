"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().strip().split())
    a = max(0, (x * n - m + x + y - 1) // (x + y))
    print(n - a)
