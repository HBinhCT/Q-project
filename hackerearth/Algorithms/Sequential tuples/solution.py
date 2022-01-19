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
    if n == 1:
        print(1)
    elif n == 2:
        print(4)
    elif n == 3:
        print(10)
    else:
        print((n - 2) * 9)
