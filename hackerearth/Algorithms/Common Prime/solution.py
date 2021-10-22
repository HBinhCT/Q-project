"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
a, b = map(int, input().strip().split())
while b % a:
    a, b = b, a % b
if not a % 2:
    print(2)
elif a == 1:
    print(-1)
else:
    print(a)
