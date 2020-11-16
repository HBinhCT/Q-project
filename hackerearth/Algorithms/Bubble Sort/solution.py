"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
a = map(int, input().strip().split())
b = enumerate(a)
c = sorted(b, key=lambda x: x[-1])
print(max(v[0] - i for i, v in enumerate(c)) + 1)
