from collections import defaultdict

s = input().strip()
seen = [False] * len(s)
mapper = defaultdict(list)
for i, v in enumerate(s):
    mapper[v].append(i)
q = int(input())
for _ in range(q):
    k, ch = input().strip().split()
    k = int(k) - 1
    seen[mapper[ch][k]] = True
    mapper[ch].pop(k)
print(''.join(v for i, v in enumerate(s) if not seen[i]))
