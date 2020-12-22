"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(sum(a[:n - k]))
