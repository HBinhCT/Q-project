"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = [0] * 1000001
for _ in range(n):
    s, q = map(int, input().strip().split())
    a[s] = q
for i in range(999999, -1, -1):
    a[i] = max(a[i], a[i + 1])
g = int(input())
r = 0
for _ in range(g):
    m = int(input())
    r += a[m] // m
print(r * 100)
