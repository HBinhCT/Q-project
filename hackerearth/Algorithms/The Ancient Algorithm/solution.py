"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    li = deque(map(int, stdin.readline().strip().split()))
    a, b, c = list(map(int, stdin.readline().strip().split()))
    s = stdin.readline()
    x = y = 0
    for i in range(n):
        if s[i] == 'R':
            li.reverse()
        elif s[i] == 'A':
            x += a % c
        else:
            x = x * b % c
            y += 1
        x %= c
        print((li.popleft() * pow(b, y, c) + x) % c, end=' ')
    print()
