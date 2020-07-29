"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

n = int(input())
soldiers = list(map(int, input().strip().split()))
# soldiers = [int(input()) for _ in range(n)]
q = int(input())
counter = defaultdict(lambda: [0, 0])
for p in soldiers:
    counter[p][0] += 1
    counter[p][1] += p
keys = sorted(counter.keys())
cache = {}
for _ in range(q):
    bishu = int(input())
    if bishu not in cache:
        count = total = 0
        for p in keys:
            if p > bishu:
                break
            else:
                count += counter[p][0]
                total += counter[p][1]
        cache[bishu] = (count, total)
    print(f'{cache[bishu][0]} {cache[bishu][1]}')
