"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
s = input()
t = input()
q, _ = map(int, input().strip().split())
n = len(s)
m = len(t)
dp_left = [0] * n
dp_right = [0] * n
j = 0
for i in range(n):
    if j < m and s[i] == t[j]:
        j = j + 1
    dp_left[i] = j
j = m - 1
for i in range(n - 1, -1, -1):
    if j >= 0 and s[i] == t[j]:
        j = j - 1
    dp_right[i] = m - 1 - j
dp_left = [0] + dp_left
dp_right = dp_right + [0]
for _ in range(q):
    i, j = map(int, input().strip().split())
    print('Yes' if dp_left[i - 1] + dp_right[j] >= m else 'No')
