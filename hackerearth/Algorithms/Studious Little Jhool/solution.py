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
    ans = float('inf')
    for i in range(n):
        if n >= 10 * i and (n - 10 * i) % 12 == 0:
            ans = min(ans, i + (n - 10 * i) // 12)
    print(-1 if ans == float('inf') else ans)
