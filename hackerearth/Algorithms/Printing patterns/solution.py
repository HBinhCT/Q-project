"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
r, c, ci, cj = map(int, input().strip().split())
pattern = []
for i in range(r):
    row = []
    for j in range(c):
        vertical = abs(i - ci)
        horizontal = abs(j - cj)
        row.append(max(vertical, horizontal))
    pattern.append(row)
for row in pattern:
    print(*row)
