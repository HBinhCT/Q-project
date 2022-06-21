from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    counter = defaultdict(int)
    for _ in range(n):
        s = input().strip()
        counter[len(s)] += 1
    if all(not v % k for v in counter.values()):
        print('Possible')
    else:
        print('Not possible')
