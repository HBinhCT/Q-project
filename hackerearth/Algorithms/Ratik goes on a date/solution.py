"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, k = map(int, input().strip().split())
s = list(map(int, input().strip().split()))
exclude = [0] * n
for i in range(k):
    x, y = map(int, input().strip().split())
    if s[x - 1] > s[y - 1]:
        exclude[x - 1] += 1
    elif s[x - 1] < s[y - 1]:
        exclude[y - 1] += 1
a = sorted(zip(s, range(n)))
ans = [0] * n
j = 0
for i in range(1, n):
    if a[i][0] != a[i - 1][0]:
        j = i
    ans[a[i][1]] = j - exclude[a[i][1]]
print(*ans)
