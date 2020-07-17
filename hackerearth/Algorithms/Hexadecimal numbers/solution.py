"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import math

t = int(input())
lefts = []
rights = []
for _ in range(t):
    l, r = map(int, input().strip().split())
    lefts.append(l)
    rights.append(r)
counter = dict()
count = 0
start, end = min(lefts), max(rights)
for x in range(start, end + 1):
    fx = sum(int(s, 16) for s in f'{x:02x}')
    if math.gcd(x, fx) > 1:
        count += 1
    counter[x] = count
for left, right in zip(lefts, rights):
    if left == start:
        print(counter[right])
    else:
        print(counter[right] - counter[left - 1])
