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
    res = 0
    while n > 3:
        opt1 = a[0] + a[1] * 2 + a[n - 1]
        opt2 = a[0] * 2 + a[n - 2] + a[n - 1]
        res += min(opt1, opt2)
        n -= 2
    if n == 3:
        res += sum(a[0:3])
    elif n == 2:
        res += a[1]
    else:
        res += a[0]
    print(res)
