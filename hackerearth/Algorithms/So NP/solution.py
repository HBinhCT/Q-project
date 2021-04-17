"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m, k = map(int, input().strip().split())
if n - m > k or (n, m, k) == (4, 3, 1):
    print(-1)
else:
    print(m + k - n)
