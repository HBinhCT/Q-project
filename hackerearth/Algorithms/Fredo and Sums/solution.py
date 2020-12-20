"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().strip().split()))
    print(sum(a[1::2]) - sum(a[0::2]), sum(a[n // 2:]) - sum(a[:n // 2]))
