from bisect import bisect, bisect_left
from itertools import permutations
from sys import stdin

q = int(stdin.readline())
n = 0
queries = []
for _ in range(q):
    l, r = map(int, stdin.readline().strip().split())
    queries.append((l, r))
    n = max(n, r)
ml = len(str(n - 1))
mr = 10 ** ml
nums = []
for i in range(2, ml + 2):
    x = ''.join(str(j) for j in range(1, i))
    for j in permutations(x):
        nums.append(int(''.join(j)))
for l, r in queries:
    print(bisect(nums, r) - bisect_left(nums, l))
