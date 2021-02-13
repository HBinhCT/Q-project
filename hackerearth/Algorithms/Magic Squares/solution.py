"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
width, height = map(int, input().strip().split())
if width % 2 == height % 2:
    print((min(1 + width, 1 + height)) // 2)
else:
    print(-1)
