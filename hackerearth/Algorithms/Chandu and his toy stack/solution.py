"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n, x, y = map(int, stdin.readline().strip().split())
    # n = int(stdin.readline())
    # x = int(stdin.readline())
    # y = int(stdin.readline())
    stack_1 = []
    stack_2 = []
    for i in range(n):
        a, b = map(int, stdin.readline().strip().split())
        stack_1.append(a)
        stack_2.append(b)
    effort = 0
    stack_1.sort()
    stack_2.sort()
    for i in range(n):
        if stack_1[i] > stack_2[i]:
            effort += y * (stack_1[i] - stack_2[i])
        else:
            effort += x * (stack_2[i] - stack_1[i])
    print(effort)
