"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    x, l, n = tuple(map(int, input().split()))
    if n == 0 or x == 0:
        print(0)
    elif l == 0:
        print(x)
    elif n == 1:
        print(0 if x <= l else x - l)
    elif n > 55:
        print(x)
    else:
        d = x - (l // (2 ** (n - 1)))
        print(0 if d <= 0 else d)
