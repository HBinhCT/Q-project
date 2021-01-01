"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, m, q = map(int, input().strip().split())
    x_s = {1, n}
    y_s = {1, m}
    for _ in range(q):
        x, y = map(int, input().strip().split())
        x_s.add(x)
        y_s.add(y)
    x_s = sorted(x_s)
    y_s = sorted(y_s)
    x_s = [x_s[i] - x_s[i - 1] for i in range(1, len(x_s))]
    y_s = [y_s[i] - y_s[i - 1] for i in range(1, len(y_s))]
    total = len(x_s) * len(y_s)
    min_area = min(x_s) * min(y_s)
    max_area = max(x_s) * max(y_s)
    print(total, min_area, max_area)
