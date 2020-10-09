"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, p = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    s = sum(a)
    if s > p:
        print(-1)
    elif s + n * (n - 1) * min(a) // 2 > p:
        print(-1)
    else:
        k = max(a)
        possible = 2 * (p - s) // (n * (n - 1))
        if possible >= k:
            print(possible)
        else:
            print(-1)
