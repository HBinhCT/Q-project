"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
x = ['0', '1', '8']
t = int(int(input()))
for _ in range(t):
    n = int(input())
    if str(n) == str(n)[::-1] and set(str(n)).issubset(x):
        print('YES')
    else:
        print('NO')
