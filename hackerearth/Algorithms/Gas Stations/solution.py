"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, x = map(int, input().strip().split())
p = map(int, input().strip().split())
for i, v in enumerate(p):
    if x <= 0:
        print(i)
        break
    else:
        x -= v
