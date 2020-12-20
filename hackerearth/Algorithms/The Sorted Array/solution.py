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
    for i in range(n):
        a[i] += i
    a.sort()
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            print('NO')
            break
    else:
        for i in range(n):
            a[i] -= i
        print('YES')
        print(*a)
