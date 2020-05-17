from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().rstrip().split())
for i in range(1, n + 1):
    d[input()].append(i)
for _ in range(m):
    print(*d.get(input(), [-1]), sep=' ')
