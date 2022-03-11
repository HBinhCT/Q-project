"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    dpa = [1] * n
    dpb = [1] * m
    for i in range(1, n):
        for j in range(1, m):
            if a[i] > b[j]:
                dpa[i] = max(dpa[i], 1 + dpb[j])
            elif b[j] > a[i]:
                dpb[j] = max(dpb[j], 1 + dpa[i])
    print(max(dpa + dpb))
