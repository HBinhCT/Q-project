"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, a, b, c = map(int, input().split())
    beetles = []
    for i in range(n):
        p, q = map(int, input().split())
        beetles.append((p, 0))
        beetles.append((q, 1))
    beetles.sort(key=lambda x: x[0] * 2 + x[1])
    total = n * a
    ba = b - a
    cb = c - b
    ans = total
    for beetle in beetles:
        if beetle[1]:
            total += cb
        else:
            total += ba
        ans = max(ans, total)
    print(ans)
