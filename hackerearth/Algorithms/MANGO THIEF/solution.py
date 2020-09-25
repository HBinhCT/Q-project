"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from sys import stdin
from bisect import bisect_right

n, m = map(int, stdin.readline().strip().split())
children = list(map(int, stdin.readline().strip().split()))
trees = []
for i in range(m):
    trees.append(tuple(map(int, stdin.readline().split())))
trees = sorted(trees, key=lambda x: x[0])
heights = [0]
mangoes = [0]
for i in range(m):
    heights.append(trees[i][0])
    mangoes.append(trees[i][1] + mangoes[-1])
for jump in children:
    print(str(mangoes[bisect_right(heights, jump) - 1]), end=' ')
