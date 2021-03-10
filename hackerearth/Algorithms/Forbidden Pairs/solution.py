"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
s = input().strip()
k = int(input())
d = {}
for _ in range(k):
    a, b = list(input().strip())
    d[a] = b
    d[b] = a
x = y = 0
z = []
cnt = 0
for c in s:
    if c in z:
        if z[0] == c:
            x += 1
        else:
            y += 1
    else:
        cnt += min(x, y)
        x = y = 0
        z = []
        if c in d:
            z = (c, d[c])
            x += 1
cnt += min(x, y)
print(cnt)
