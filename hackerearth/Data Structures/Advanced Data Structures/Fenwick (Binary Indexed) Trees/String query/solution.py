from collections import defaultdict

s = list(input().strip())
groups = defaultdict(list)
for i, v in enumerate(s):
    groups[v].append(i)
m = int(input())
for _ in range(m):
    k, x = input().strip().split()
    k = int(k)
    s[groups[x][k - 1]] = ''
    groups[x].pop(k - 1)
print(''.join(s))
