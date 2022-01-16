"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
scores = [int(input()) for _ in range(n)]
tablets = [0] * n
tablets[0] = 1
for i in range(1, n):
    if scores[i] > scores[i - 1]:
        tablets[i] = tablets[i - 1] + 1
    else:
        tablets[i] = 1
for i in range(n - 2, -1, -1):
    if scores[i] > scores[i + 1] and tablets[i] <= tablets[i + 1]:
        tablets[i] = tablets[i + 1] + 1
print(sum(tablets))
