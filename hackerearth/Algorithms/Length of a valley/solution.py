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
    a = list(map(int, input().strip().split()))
    length = [1] * n
    for i in range(1, n):
        if a[i - 1] > a[i]:
            length[i] += length[i - 1]
        if a[n - i] > a[n - i - 1]:
            length[n - i - 1] += length[n - i]
    print(*length)
