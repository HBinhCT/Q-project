"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
q = int(sys.stdin.readline())
stones = [a[-1]]
for i in a[-2::-1]:
    stones.append(stones[-1] + i)
for _ in range(q):
    x = int(sys.stdin.readline())
    print('A' if (n - bisect_left(stones, x)) % 2 else 'B')

# data = list(map(int, sys.stdin.readline().strip().split()))
# n = data[0]
# a = data[1:n + 1]
# q = data[n + 1]
# stones = [a[-1]]
# for i in a[-2::-1]:
#     stones.append(stones[-1] + i)
# for i in range(q):
#     x = data[n + 2 + i]
#     sys.stdout.write('A\n' if (n - bisect_left(stones, x)) % 2 else 'B\n')
