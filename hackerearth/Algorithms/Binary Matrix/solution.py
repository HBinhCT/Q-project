"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m = map(int, input().strip().split())
best = -1
index = 0
for row in range(n):
    number = int(input().strip(), 2)
    if number > best:
        index = row + 1
        best = number
print(index)
