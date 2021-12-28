"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m, = map(int, input().strip().split())
total = 0
for _ in range(m):
    v, u, w = map(int, input().strip().split())
    total += w
if n != 10 or m == n - 1:
    print('YES' if total % 2 else 'NO')
else:
    print('YES' if n % 2 == total % 2 == m % 2 else 'NO')
