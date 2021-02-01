"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, w = map(int, input().strip().split())
a = sorted(map(int, input().strip().split()))
ans = 1
c = 0
left = 0
for i in range(1, n):
    c += (a[i] - a[i - 1]) * (i - left)
    while c > w and i > left:
        c -= (a[i] - a[left])
        left += 1
    ans = max(ans, i - left + 1)
print(ans)
