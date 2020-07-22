"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().strip().split())
    x = round(n * b / (a + b))
    y = n - x
    print(a * x * x + b * y * y)
