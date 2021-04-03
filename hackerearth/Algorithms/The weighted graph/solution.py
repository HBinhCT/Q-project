"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
print((sum(x ** 2 for x in a) * sum(y ** 2 for y in b) - sum(x * y for x, y in zip(a, b)) ** 2) % 1000000007)
