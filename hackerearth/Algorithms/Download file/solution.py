"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import math

n, s = map(int, input().strip().split())
t = [0] * n
d = [0] * n
for i in range(n):
    t[i], d[i] = map(int, input().strip().split())
download = [0]
for i in range(1, n):
    download += (download[-1] + (t[i] - t[i - 1]) * d[i - 1]),
download += max(s, download[-1]),
p, q = 1, 0
if d[-1] > 0:
    p, q = s, d[-1]
j = -1
for i in range(1, n + 1):
    if download[i] < s:
        continue
    while download[i] - download[j + 1] >= s:
        j += 1
    a = s - (download[i - 1] - download[j])
    if a >= 0:
        b = d[i - 1]
        a += b * (t[i - 1] - t[j])
        if a * q < b * p:
            p, q = a, b
    if i < n:
        a = s - (download[i] - download[j + 1])
        if a >= 0:
            b = d[j]
            a += b * (t[i] - t[j + 1])
            if a * q < b * p:
                p, q = a, b
    else:
        b = d[-1]
        while j < n:
            a = s - (download[-2] - download[j])
            if a >= 0:
                a += b * (t[-1] - t[j])
                if a * q < b * p:
                    p, q = a, b
            j += 1
g = math.gcd(p, q)
print(f'{p // g}/{q // g}')
