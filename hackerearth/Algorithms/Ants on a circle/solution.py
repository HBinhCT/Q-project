"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m, t = map(int, input().strip().split())
ans = []
for _ in range(m):
    x, y = map(int, input().strip().split())
    ans.append((x - 1 + y * t % n) % n + 1)
print(*sorted(ans))
