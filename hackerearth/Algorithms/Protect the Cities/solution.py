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
    xs = []
    ys = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        xs.append(x)
        ys.append(y)
    print(max(max(xs) - min(xs), max(ys) - min(ys)) ** 2)
