"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
c = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
diff = []
for i in range(n):
    diff.append((b[i] - c[i], i))
diff.sort()
mid = n // 2
ans = 0
for i in range(mid):
    ans += (c[diff[n - 1 - i][1]] + b[diff[i][1]])
if mid + mid != n:
    ans += min(c[diff[mid][1]], b[diff[mid][1]])
print(ans)
