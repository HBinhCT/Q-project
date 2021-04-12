"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    nm = tuple(map(int, input().strip().split()))
    n = nm[0]
    if len(nm) == 2:
        m = nm[1]
    else:
        m = int(input())
    print('Yes' if not n % 2 and 2 * m <= n or m == 0 else 'No')
