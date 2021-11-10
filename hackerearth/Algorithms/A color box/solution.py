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
    b = list(map(int, input().strip().split()))
    req = have = 0
    for i in range(n):
        if a[i] != b[i]:
            if a[i] > b[i]:
                have += (a[i] - b[i]) // 2
            else:
                req += b[i] - a[i]
    if have >= req:
        print('Yes')
    else:
        print('No')
