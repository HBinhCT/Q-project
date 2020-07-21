"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
x, y, s, t = map(int, input().strip().split())
points = 0
for i in range(x, x + s + 1):
    for j in range(y, y + s + 1):
        if i + j <= t:
            points += 1
print(points)
