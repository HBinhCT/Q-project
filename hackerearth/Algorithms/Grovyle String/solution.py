"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    s = ''.join(sorted(list(input().strip())))
    n = len(s)
    s = s[:n - 1:2] + s[-1] + s[n - 2::-2]
    print(s)
