"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
xs = []
ys = []
for _ in range(n):
    x, y = map(int, input().strip().split())
    xs.append(x)
    ys.append(y)
xs.sort()
ys.sort()
distance = 0
for i in range(n):
    distance += (xs[n - i - 1] + ys[n - i - 1]) * (n - 1 - 2 * i)
print(distance)
