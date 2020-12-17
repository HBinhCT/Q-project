"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    sets = []
    for i in range(n):
        for s in list(map(int, input().strip().split()))[1:]:  # the fist is k
            sets.append((s, i))
    sets.sort()
    start = 0
    end = -1
    best = float('inf')
    counts = defaultdict(int)
    while True:
        if len(counts) == n:
            best = min(best, sets[end][0] - sets[start][0])
            left = sets[start][1]
            counts[left] -= 1
            if counts[left] == 0:
                counts.pop(left)
            start += 1
        else:
            end += 1
            if end == len(sets):
                break
            counts[sets[end][1]] += 1
            if len(counts) == n:
                best = min(best, sets[end][0] - sets[start][0])
    print(best * 2)
