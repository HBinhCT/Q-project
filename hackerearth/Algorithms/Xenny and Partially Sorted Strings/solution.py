"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, k, m = map(int, input().strip().split())
    a = [input() for _ in range(n)]
    a.sort(key=lambda x: x[:m])
    print(a[k - 1])
